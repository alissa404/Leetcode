'''
為什麼「要用兩個 stack」

Stack 是後進先出LIFO

但 Queue 是先進先出FIFO

👉 **Queue一定要「反轉一次順序」**

'''

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    
# 時間複雜度 : amortized O(1) 空間複雜度：O(n)

'''
為什麼是 amortized O(1)？
「一個元素的一生」
被 push 進 in_stack 1 次
最多只會被倒一次 → out_stack
被 pop 出 out_stack 1 次
👉 每個元素最多被移動 2 次

總成本
n 個元素 → n 次操作
n 次 queue 操作 → 平均 O(1)
👉 amortized O(1)
worst case O(n)
'''
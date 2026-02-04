class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 避免list 長度太短
        if not head or not head.next:
            return

        slow, fast = head, head
        # 當 fast.next.next 走到底時，走完那一輪的 slow，slow 會剛好指在一半的位置
        while fast and fast.next:
            slow = slow.next # slow = 3
            fast = fast.next.next  # fast = 5

        # 把後半存成一個新的list 叫做second
        second = slow.next
        # 切開前後半
        slow.next = None  


        # Step 2: 反轉後半段(second)
        prev = None
        cur = second # second = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        second_new = prev  


        # Step 3: 交錯合併
        first, second_list = head, second_new
        '''
        first = 1
        second_list = 5
        tmp1 = first.next = 2
        tmp2 = second_list.next = 4
        '''
        while second_list:
            # 暫存 next
            tmp1 = first.next
            tmp2 = second_list.next

            # 交錯插入
            first.next = second_list # 1 -> 5
            second_list.next = tmp1 # 1 -> 5 -> 2

            # 移動指標
            first = tmp1 # first = 2
            second_list = tmp2 # second_list = 4

            # 空間複雜度：O(1)
            # 時間複雜度：O(n)

def build_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


head_list = [1, 2, 3, 4, 5]
head = build_list(head_list)
solver = Solution()
solver.reorderList(head)   
print_list(head) 

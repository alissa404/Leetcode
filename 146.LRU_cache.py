# double linked list + hashmap

# 宣告一個node 
class Node:
    def __init__(self, key, value):
        # 存 key 是為了在doubly linked list刪除時，能找回 HashMap 的 Key
        self.key = key     
        self.val = value
        self.prev = None
        self.next = None 
        # prev -> node -> next

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {} 

        # "LRUCache" = 2 = capacity 只能放兩個值
        self.capacity = capacity

        # 建立虛擬節點
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right # 因為capacity內 只有兩個值
        self.right.prev = self.left # 所以左邊的下一個就是右邊，右邊的前一個就是左邊
        
    def remove(self, node):
        """從雙向鏈結串列中 刪除某個節點"""
        # 先定義好 prev -> node -> next
        prev_node = node.prev
        next_node = node.next
        # node 不見了(被刪掉)
        prev_node.next = next_node
        next_node.prev = prev_node


    def insert(self, node):
        """
        insert node before right node (表示最近剛使用過) 
        新的node要牽prev node 和 right node 的手
        原本在那裡的兩個人的手都要牽回 node
        """
        # prev_node -> node -> right(next_node) 
        # 先以 right 為基準 去定義 prev_node, next_node
        prev_node = self.right.prev
        next_node = self.right

        # 讓 node 的兩隻手去牽prev_node, next_node
        node.next = next_node
        node.prev = prev_node
        
        # 讓這兩個人也回牽 node (這是你原本漏掉的！)
        prev_node.next = node
        next_node.prev = node


    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key]) 
            '''
            為何要 remove 再 insert? 為了refresh get 到的值。
            假設[1, 2]（1 是最舊的，2 是最新的）。
            你頻繁地執行 get(1)。
            如果你沒有 remove(1) 再 insert(1)，1 就會一直待在最舊的位置。
            當下一個 put(3, 3)，系統看到 1 在最左邊（最舊），就會把明明你最常用的 1 給踢掉。
            '''
            return self.hashmap[key].val

        return -1 # hashmap 裡面沒有這個key


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # remove the least recently used key
            self.remove(self.hashmap[key])

        # 寫入hashmap
        self.hashmap[key] = Node(key,value) # 新增一個node in hashmap
        self.insert(self.hashmap[key]) # 新增一個node in doubly linked list

        if len(self.hashmap) > self.capacity:
            # 找出最久沒使用的節點 (self.left 是虛擬節點（不存資料）self.left.next 才是最舊的資料)
            lru = self.left.next

            # 從鏈結串列中移除
            self.remove(lru) 
            
            #刪除 HashMap 裡的 Key
            del self.hashmap[lru.key] #lru is a node
            '''
            如果你只做了 self.remove(lru)，在鏈結串列 確實找不到它了，
            但 hashmap 是根據 Key 來找人的。
            若沒有del self.hashmap[lru.key]，下一次 get(key) 的時候，
            HashMap 會回傳一個已經不在鏈結串列裡的孤兒節點，整個程式邏輯崩潰。
            '''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
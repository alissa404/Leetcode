class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        dummy.val = 0
        dummy.next = head
        怕要移除的node 是head, 所以要設定一個dummy node 指向head
        如果要刪除 head，slow 就會乖乖停在 dummy，所以初始值要設定在dummy
        '''
        dummy = ListNode(val=0, next=head)
        slow = dummy
        fast = dummy
        
        # fast 先走 n 步，之後跟slow 一起都只動一步，最終slow 就會指向倒數第n 個節點
        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow 下一個就是要被移除的節點
        slow.next = slow.next.next

        return dummy.next

# 時間 O(n)
# 空間 O(1) 

def build_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)
    
nums = [1,2,3,4,5]
n = 2
head = build_list(nums)

sol = Solution()
new_head = sol.removeNthFromEnd(head, n)
print_list(new_head)
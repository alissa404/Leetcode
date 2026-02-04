class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        cur = head
        pre = None

        while cur:
            # 先定義好cur 的下一個叫做 nxt
            nxt = cur.next

            # 先動指標 將 cur.next 指向 pre
            cur.next = pre
            pre = cur
            cur = nxt #現在cur 跑到nxt了
            
        return pre

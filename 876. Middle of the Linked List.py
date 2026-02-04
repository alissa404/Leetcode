# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 雙指標 快慢指標 找中間點
        # 當快指標 (一次走兩步)走到終點時就停止
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 回傳slow -> 指向的節點(後面自然就會接上手裡還牽著的後面節點)
        return slow
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dummy.next = head
        
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: 從 prev 之後開始反轉
        cur = prev.next
        for _ in range(right - left):
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
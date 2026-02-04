'''
如果 list 形成環，
快指針（一次走 2 步）
跟
慢指針（一次走 1 步）
最終一定會相遇。
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
# 空間複雜度：O(1) 時間複雜度：O(n)
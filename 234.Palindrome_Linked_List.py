# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Step 1: find middle
        slow = fast = head  # 兩個都在第一個數值
        
        while fast and fast.next:
            slow = slow.next # 走一步
            fast = fast.next.next # 走兩步

        # Step 2: skip middle if odd
        if fast != None:
            slow = slow.next       

        # Step 3: reverse second half
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # Step 4: compare
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# two pointers 時間 O(n)、空間 O(1)
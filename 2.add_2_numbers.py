class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        cur = dummy

        while (l1!=None or l2!=None):
            if not l1:
                sum = carry + l2.val
            elif not l2:
                sum = carry + l1.val
            else:
                sum = carry + l1.val + l2.val

            carry = sum // 10
            sum = int(sum % 10)

            newNode = ListNode(sum) # create a node, node.val = sum
            cur.next = newNode
            cur = cur.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        # 最後一個還有進位
        if carry == 1:  
            cur.next = ListNode(carry) # create a node, node.val = carry

        return dummy.next
    
# time O(n)
# space O(1)
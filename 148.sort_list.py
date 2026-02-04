# linked list 最適合使用 Merge Sort 來解

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: split list
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None  # cut

        # Step 2: sort both halves
        left = self.sortList(head) #原始起點
        right = self.sortList(slow) #另一半的起點

        # Step 3: merge
        return self.merge(left, right)


    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val: 
                print(f"  pick {l1.val} from left") #step 2 : l1 = 2 / l2 = 3 , pick 2 from left
                cur.next = l1
                l1 = l1.next
            else:
                print(f"  pick {l2.val} from right") #step 1 : l1 = 2 / l2 = 1 , pick 1 from right
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        print("  merged:", self.to_list(dummy.next))
        return dummy.next
    

    def to_list(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res


def build_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


head_list = [4,2,1,3]
head = build_list(head_list)
solver = Solution()
solver.sortList(head)   


# 時間：O(n log n) 空間：O(1)
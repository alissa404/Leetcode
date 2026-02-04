# 方法一
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while (l1!=None and l2!=None):
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next 

            # 移動 current 指標到下一個位址
            cur = cur.next   

        # l1 or l2 is empty
        cur.next = l1 or l2
        return dummy.next
    
# 空間複雜度：O(1)
# 時間複雜度：O(n + m)

# 方法二
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None or list2==None:
            return list1 or list2
        if list1.val <= list2.val: #先處理小的
            list1.next = self.mergeTwoLists(list2, list1.next)
            return list1 #小的先
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
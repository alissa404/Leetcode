# Merge sort (divide and conquer) 
# or MinHeap

from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# merge sort
class Solution:
    def mergeKLists_merge_sort(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if not lists:
            return None
        return self._merge_range(lists, 0, k-1)

    # 把 lists[l:r] 左右對半拆開，左右各自 merge sort，再兩兩合併
    def _merge_range(self, lists, left, right) -> Optional[ListNode]:
        
        # 若區間內只剩一條 list，直接回傳
        if left == right:
            return lists[left]
        
        mid = (left + right) // 2
        # 左半邊合成一條 sorted list
        l = self._merge_range(lists, left, mid)
        # 右半邊合成一條 sorted list
        r = self._merge_range(lists, mid + 1, right)

        # 再把兩條 sorted list 合併
        return self._merge_two_lists(l, r)

    # 合併兩條 sorted linked list：時間 O(m+n)，空間 O(1)
    '''
    m = l1 這條 linked list 的節點數
    n = l2 這條 linked list 的節點數
    '''
    def _merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        '''
        結果: 1 → 2 → 3
        l1: 4 → 7 → None
        l2: None
        '''
        # 如果 l1 還沒走完，就把整條 l1 接上來；否則就把整條 l2 接上來。
        tail.next = l1 if l1 else l2
        return dummy.next

# 時間都是 O(N log k)
# 空間 O(log k)
# k = lists 的條數
# N = 所有 list 的總節點數（全部 node 數加總）

##################################################################################

    # min heap

    def mergeKLists_min_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # 把每條 list 的 head 丟進 heap
        # (node.val, idx, node) 裡的 idx 是為了避免 val 相同時 ListNode 無法比較
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)

            # 接到答案尾端
            tail.next = node
            tail = tail.next

            # 把該節點的下一個丟回 heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # 保險：避免最後 tail 還指向舊鏈結（通常不需要，但可讓鏈結更乾淨）
        tail.next = None
        return dummy.next


lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists1 = [build_linked_list(a) for a in lists]
ans1 = Solution().mergeKLists_merge_sort(linked_lists1)
print(linked_list_to_list(ans1))

linked_lists2 = [build_linked_list(a) for a in lists]
ans2 = Solution().mergeKLists_min_heap(linked_lists2)
print(linked_list_to_list(ans2))

#時間 O(N log k)
#空間 O(k)
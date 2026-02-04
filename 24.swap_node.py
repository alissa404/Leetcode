class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # ListNode(0, head) 會幫你把新建立的 dummy 節點 「接上」 原本的火車 List
        # 若是用 ListNode(0) 只是建立了一個 「孤立」 的車頭。
        dummy = ListNode(0, head)
        
        # pre =「當前要 swap 的那一組的前一個節點」
        # 每一次 swap，都需要「前一個節點」來重新接回鏈結
        pre = dummy  # 後面就會變成 dummy != pre

        # 不可以定義在 while 外面，因為pre 會移動
        # slow = pre.next
        # fast = pre.next.next

        # dummy 永遠不會動
        while pre.next and pre.next.next:
            slow = pre.next
            fast = pre.next.next

            '''
            dummy/pre → 1 → 2 → 3 → 4
                         ↑   ↑
                        slow fast
            '''

            # swap
            slow.next = fast.next  # 1 → 3 → 4
            fast.next = slow  # 2 → 1 → 3 → 4 
            pre.next = fast  # pre → 2 → 1 → 3 → 4
 
            # move pre
            pre = slow

            '''
            第一次 swap
            pre = dummy

            結果：
            dummy → 2 → 1 → 3 → 4
                        ↑
                        pre
            
            pre 移動，此時 dummy != pre
            '''

        return dummy.next

# 空間: O(1)     
# 時間: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None

        def inorder(node):
            if not node or self.ans is not None: # 已經是 k=0 且得到ans，就直接跳出
                return

            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.ans = node.val  # 得到ans
                return
            
            inorder(node.right)  #沒有得到ans 就執行右邊的樹

        inorder(root)
        return self.ans


# DFS inorder 解法
# 時間	O(h + k)（走到第 k 個就停）
# 空間	O(h)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# LCA 使用DFS postorder 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        '''
        left / right 的意義是：
        1. None → 這個子樹 沒有 p 或 q
        2. p 或 q 或某個節點 → 這個子樹 有找到 p 或 q
        '''
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        '''
        左子樹有找到東西 而且 右子樹也有找到東西 那這時候誰是最近公共祖先？👉 就是現在這個 root
        '''
        if left and right:
            return root

        '''
        「如果只有一邊有找到東西，就把那一邊的結果往上傳。」
        '''
        return left if left else right

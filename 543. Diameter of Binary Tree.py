# DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
          1 (Root)
         / \
        2   X
       / \
      3   4
     /     \
    5       6
    最大長度不是 root 到最深leaf node 的距離，而是轉折的總長度
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        # DFS get max_depth
        def get_depth(node):
            if not node: return 0
            
            ll = get_depth(node.left)
            rr = get_depth(node.right)

            # 目前以 input node 為 root 來看的最長路徑
            # 我們最終要回傳的答案
            self.max_depth = max(self.max_depth, ll + rr)
            
            # return self.max_depth
            return 1 + max(ll, rr) # 回傳input node 所在的高度是多少，好讓父節點去計算總高度

        # 回傳這棵樹的 「總高度」（從根節點到最深葉子的距離)
        get_depth(root)

        # return get_depth(root)        
        return self.max_depth

# time : O(n)
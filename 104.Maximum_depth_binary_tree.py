class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        '''
        OOP 
        記得要用self. 因為是包在 class 裡面的 def function，要呼叫自己的話，
        在python 不加self. 就會從class 外面去找這個 def function，
        但是我們是定義在 class 內，所以要記得用 self.

        class 裡面的def 裡面的 def 不用加 self.
        舉例我們定義
        class Solution:
            def maxDepth():
                def get_depth():
                    left_depth = get_depth() 這樣就不用加self.

        '''
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
      
        return 1 + max(left_depth, right_depth)

root = [3,9,20,null,null,15,7]
Solution().maxDepth(root)
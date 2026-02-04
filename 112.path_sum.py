# DFS recursion
# traversal order（in-order / pre-order）不是重點，使用 DFS 遞迴就可

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # 到 leaf node，檢查targetSum=0 ?
        if not root.left and not root.right:
            if targetSum == root.val:
                return True # 表示剩下的值剛剛好
            else : return False
        
        print(root.val, 'node')
        print(targetSum - root.val)
        return (
            self.hasPathSum(root.left, targetSum - root.val) or 
            self.hasPathSum(root.right, targetSum - root.val)
        )
               
from collections import deque

def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root

'''
        5
      /   \
     4     8
    /     / \
   11    13  4
  /  \         \
 7    2         1
'''
arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
root = build_tree(arr)
print(Solution().hasPathSum(root, targetSum))

'''
進到 root 5
hasPathSum(5, 22)
不是 leaf node
進到 targetSum：22 - 5 = 17
hasPathSum(4, 17)
...
hasPathSum(7, 2)
✅ leaf（沒有左右子樹）
targetSum == node.val → 2 == 7 ❌回傳 False

回到節點 11，因為 left 是 False，所以繼續走 right
targetSum == node.val → 2 == 2 ✅回傳 True

7 → 11 → 4 這條不行 因為沒有root-to-leaf 
'''
# DFS post order

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1

    def height(self, node):
        if not node:
            return 0 # 空樹
        print(node.val, "init")

        left = self.height(node.left)
        print(node.val, "val")
        print(left, "left")

        if left == -1:
            return -1 # 左子樹已不平衡 early stop

        right = self.height(node.right)
        print(node.val, "val")
        print(right, "right", '\n')
        if right == -1:
            return -1 # 右子樹已不平衡

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1


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
        1
      /   \
     2     2
    / \
   3   3
  / \
 4   4
'''
arr = [1,2,2,3,3,None,None,4,4]
root = build_tree(arr)
print(Solution().isBalanced(root))  

# time O(n)
# space O(h)
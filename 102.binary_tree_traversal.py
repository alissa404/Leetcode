from collections import deque

# BFS
class Solution:
    def BFS_levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        res = []
        queue = deque([root]) # root 放進queue
        while queue:
            level = []
            for _ in range(len(queue)): # 算出這一層有多少節點 只處理屬於這一層的節點
                node = queue.popleft()
                level.append(node.val)

                print('level', level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level) #將這一層的結果存入 res
            print('r',res)

        return res

# 時間: O(n)
# 空間: O(n)

##############################################################################

    # DFS
    def DFS_levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        result = []            
        def dfs(level, node):
            print(len(result) - 1)
            if level > len(result) - 1:
                result.append([])

            result[level].append(node.val)
            if node.left:
                dfs(level+1, node.left)
            if node.right:
                dfs(level+1, node.right)

        dfs(0, root)
        return result


# 時間: O(n)
# 空間: O(n)

##############################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().BFS_levelOrder(root))

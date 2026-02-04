# DFS

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        # 遞迴處理左子樹與右子樹
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

##############################################################################

# BFS

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        # deque() 的括號內必須放Iterable的東西
        # 當 q = deque(root) deque 會試圖把 root 拆開。
        # 但 root 是一個 TreeNode 物件，不是一個列表或字串，Not Iterable
        # 舉例 deque((node1, node2))
        q = deque([root])

        while q:
            node = q.popleft()
            
            # 這樣可行是涉及到 Python 的一個特殊機制：
            # Tuple Packing (元組打包) 與 Unpacking (拆解)
            node.left, node.right = node.right, node.left

            # 分開兩行會失敗
            # node.left= node.right
            # node.right = node.left

            # 把子節點放進 queue，等一下換它們當主角
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
    
# time : O(n)

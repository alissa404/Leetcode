# DFS + Hashmap
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        mp = {} #Python 的 dict 就當 HashMap 用即可

        def dfs(cur):
            if cur in mp:
                return mp[cur] #都走過了

            copy = Node(cur.val)
            mp[cur] = copy
            for nei in cur.neighbors:
                #把「鄰居的 clone 節點」加進「目前節點的 clone 的 neighbors」
                copy.neighbors.append(dfs(nei)) 
                # 為甚麼是append(dfs(nei)) 因為鄰居本身也可能還沒被 clone
            return copy

        return dfs(node)            

# time O(V + E) 每個節點最多 clone 一次 + 每條邊（每個 neighbor 關係）最多處理一次（或常數次）
# space O(V)
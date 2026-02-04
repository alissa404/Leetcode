# DAG -> topological sort 

from typing import List
from collections import deque

class Solution:

    # BFS(Queue) Kahn’s Algorithm
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 1) build graph + indegree
        graph = [[] for _ in range(numCourses)]   # 建立 numCourses 個的空列表來當graph
        indegree = [0] * numCourses

        for a, b in prerequisites:
            print("a:",a,"b:",b)
            graph[b].append(a)   # 先修 b → 才能修 a
            print(graph)

            indegree[a] += 1 # indegree[a] 表示有多少條邊指向 a


        # 2) init queue with courses that have no prerequisites
        q = deque()

        for i in range(numCourses):
            # 若沒有人指向indegree[i] 這個節點
            if indegree[i] == 0: 
                q.append(i) # 將該節點加進 queue 當中


        # 3) BFS (take courses)
        taken = 0
        while q:
            cur = q.popleft() #可直接修的課有哪些
            taken += 1
            print("cur:", cur)

            # graph[cur] 代表必須先修 cur 才能修的課
            for nxt in graph[cur]:
                print("nxt:",nxt,"\n")

                # 課 nxt 的一個先修課（cur）已經完成了，所以它還剩下的先修課數 −1
                indegree[nxt] -= 1 
                
                # 某門課已經沒有先修課了
                if indegree[nxt] == 0:
                    q.append(nxt)


        # 4) if we can take all courses, no cycle -> return True
        return taken == numCourses


##############################################################


    # DFS recursion stack
    def topo_sort_dfs(self, numCourses, graph):
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses  # 0=未訪, 1=訪問中, 2=完成
    
        def dfs(u):
            # 0=未訪, 1=訪問中, 2=完成
            if visited[u] == 1: 
                return False  # cycle
            if visited[u] == 2:
                return True

            # visited[u] == 0: 將其改成 1 
            visited[u] = 1

            # 針對 u 指向的每個節點 v 遞迴做 DFS
            for v in graph[u]: 
                if not dfs(v):
                    return False # cycle
                
            # u 指向的每個節點都被走完了，將 u 標記成完成
            visited[u] = 2
            return True
            
        for i in range(numCourses):
            # 0=未訪問過的節點
            if visited[i] == 0:
                print("before:",visited)
                if not dfs(i):
                    return False
            print("after:",visited)

        return True


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# prerequisites = [[1,0],[0,1]]

# print(Solution().canFinish(numCourses, prerequisites))
print(Solution().topo_sort_dfs(numCourses, prerequisites))

# V = node
# E = edge
# 時間 O(V + E)
# 空間 O(V + E)
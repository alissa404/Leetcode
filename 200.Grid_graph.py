'''
leetcode.200.Grid_graph 
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
'''

# DFS BFS 皆可

class Solution:

    # DFS version
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0]) # m x n matrix
        print(rows, cols)
        islands = 0

        def dfs(r, c):
            '''
            (0,0) → (0,1) → (0,2) → (0,3) → (0,4)
            ......
            (3,0) → (3,1) → (3,2) → (3,3) → (3,4)
            '''
            # out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0  # IndexError: list index out of range
            
            # water
            if grid[r][c] == '0':
                return 0

            # 把陸地標記為已訪問過
            # 若不把去過的陸地改成0，你會在陸地之間 來回重複走
            grid[r][c] = '0'

            dfs(r + 1, c)  # 往下
            dfs(r - 1, c)  # 往上
            dfs(r, c + 1)  # 往右
            dfs(r, c - 1)  # 往左

        for r in range(rows):
            for c in range(cols):
                # [0,0] [0,1] [0,2]...
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands

# R = Rows（列數）
# C = Columns（行數）
# 時間 O(R × C) = O(N)
# 空間 O(R × C) = O(N)
# 「DFS 的時間複雜度是 O(N)，N 是節點數。在 grid 中，節點數是 R×C，所以時間是 O(R×C)。」

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(Solution().numIslands(grid))
'''
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
'''
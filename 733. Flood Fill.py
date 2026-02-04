from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 用 BFS
        '''
        若 起點(sr, sc)的數值 跟 鄰居的數值 相同
        就會被影響，鄰居的數值 會被改成 color 的值
        '''
        start_color = image[sr][sc]
        
        # 如果起始位置的顏色已經是目標顏色，直接結束，避免無限迴圈
        if start_color == color:
            return image

        # tuple 要先用 list 包好，讓deque 知道這個 Tuple 是一個整體，不要拆開它
        q = deque( [(sr, sc)] )
        
        m = len(image)
        n = len(image[0])

        # 將起點染色 (這動作相當於標記為 visited)
        image[sr][sc] = color

        while q:
            # 彈出最先放進去的點
            r, c = q.popleft()

            # 上下左右 共四次
            for i in range(4) :            

                # 右 (r, c+1)
                if c + 1 < n and image[r][c+1] == start_color:
                    image[r][c+1] = color
                    q.append((r, c+1))
                    
                # 左 (r, c-1)
                if c - 1 >= 0 and image[r][c-1] == start_color:
                    image[r][c-1] = color
                    q.append((r, c-1))

                # 上 (r-1, c)
                if r - 1 >= 0 and image[r-1][c] == start_color:
                    image[r-1][c] = color
                    q.append((r-1, c))

                # 下 (r+1, c)
                if r + 1 < m and image[r+1][c] == start_color:
                    image[r+1][c] = color
                    q.append((r+1, c))

        return image
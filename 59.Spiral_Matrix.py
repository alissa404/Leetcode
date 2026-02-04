class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # 先建立 n x n 的 0 矩陣
        res = [[0] * n for _ in range(n)]

        top, height = 0, n - 1
        left, weight = 0, n - 1
        num = 1            # 要填入的當前數字
        total = n*n

        while num <= total:
            for j in range(left, weight+1):
                res[top][j] = num
                num += 1
            top += 1  # 最上面那列已經走過了

            for i in range(top, height+1):
                res[i][weight] = num   # 不懂
                num += 1
            weight -= 1  # 最右邊那欄已走過

            # 3. 從右到左：填最下面那一列 bottom
            if top <= height:  
                for col in range(weight, left - 1, -1):
                    res[height][col] = num
                    num += 1
                height -= 1  # 下邊界往上縮一格

            # 4. 從下到上：填最左邊那一欄 left
            if left <= weight:  # 邊界檢查
                for row in range(height, top - 1, -1):
                    res[row][left] = num
                    num += 1
                left += 1  # 左邊界往右縮一格

        return res
    
# 時間 O(m·n)
# 空間 O(m·n)
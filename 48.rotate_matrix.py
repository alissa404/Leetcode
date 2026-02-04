class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):   # 只跑右上角三角形
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

# - 時間 O(n²)
# - 空間 O(1)
# matrix 本來就是輸入，你修改它不算額外空間。
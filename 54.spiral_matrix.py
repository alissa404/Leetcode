class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 順時針
        # mxn matrix

        m = len(matrix)
        for i in range(m):
            n = len(matrix[i])  
       
        top = left = 0
        weight = n-1
        height = m-1

        print(m, n)
        res = []
        while left <= weight and top <= height:
            for j in range(left, weight+1):
                res.append(matrix[top][j])
            top += 1  # 最上面那列已經走過了

            for x in range(top, height+1):
                res.append(matrix[x][weight])
            weight -= 1  # 最右邊那欄已走過

            # 3. 往左：確保還有未走的 row
            if top <= height:           
                for j in range(weight, left - 1, -1):
                    res.append(matrix[height][j])
                height -= 1  # 最下面那列走過

            # 4. 往上：確保還有未走的 col
            if left <= weight:
                for i in range(height, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # 最左邊那欄走過

        return res
    
# 時間 O(m·n)
# 空間 O(m·n)
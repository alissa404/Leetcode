class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if 1 <= numRows <= 30:
            res = [[1]]

            for i in range(1, numRows):
                prev = res[-1]
                row = [1]  # 開頭永遠 1

                # 中間都是 prev[i-1] + prev[i]
                for j in range(1, i):
                    row.append(prev[j - 1] + prev[j])

                row.append(1)  # 結尾永遠 1
                res.append(row)

            return res
        
'''
時間：O(n²)

因為總共會生成 1 + 2 + … + n = n(n+1)/2 個元素

空間：O(n²)
'''
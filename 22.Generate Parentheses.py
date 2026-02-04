class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, left, right):
        
            # 終止條件為 當字串長度等於2倍的n 代表完成一小組
            if len(s) == 2 * n: 
                res.append(s)
                return

            if left < n:
                dfs(s + "(", left + 1, right) 

            if right < left:
                dfs(s + ")", left, right + 1)

        dfs("", 0, 0) # s為一個小組
        return res

n=2
sol = Solution()
print(sol.generateParenthesis(n))
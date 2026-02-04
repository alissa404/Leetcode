class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  
        res: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remain:  # 已排序，後面更大，直接剪枝
                    break
                path.append(x)          # 選擇 x
                dfs(i, remain - x)      # 可重複取用 → 下一層仍從 i 開始
                path.pop()              # 撤銷選擇

        dfs(0, target)
        return res

# 公版
path = []
def dfs(start, remain):
	for x in choices:
			path.append(x)          
			dfs()                # 繼續探索
			path.pop()           # 撤銷選擇（回到上一步）
			

candidates = [2, 3, 6, 7]
target = 7
solver = Solution()
print(solver.combinationSum(candidates, target))

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None] * len(indices)

        # 把它一個個寫進去（用res空列表接）
        for j in range(len(indices)):
            res[indices[j]] = s[j]
        
        # list 轉成 str
        return "".join(res)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sol = Solution()
print(sol.restoreString(s, indices))
# >>>leetcode

# 時間: O(n)
# 空間: O(n)
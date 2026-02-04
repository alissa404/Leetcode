# 迴文問題
# 判斷每個字母能貢獻多少「偶數對」

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)

        # 所有字母能貢獻的 偶數對 總和  
        res = 0
        for v in d.values():
            '''
            v // 2 * 2 都能幫你算出最大可用的偶數部分：
            如果 v = 3：3 // 2 * 2 = 2
            '''
            temp = (v//2) *2
            res += temp

        # 如果 res 小於原本字串長度，代表一定有剩下的奇數字母可以放在中間
        if res < len(s): return res + 1
        else: return res

        # res = sum((v // 2) * 2 for v in d.values())
        # return res + 1 if res < len(s) else res

# time O(n)
# space O(n)
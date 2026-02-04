# 用sliding window 固定視窗大小

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        res = []

        if len_s < len_p:
            return res
        
        p_count = Counter(p)
        window = Counter(s[0:len_p])  # 第一個視窗

        # 檢查第一個視窗
        if window == p_count:
            res.append(0)

        # 開始滑動視窗
        for right in range(len_p, len_s):
            # 視窗新進來一個字元 s[len_p]
            window[s[right]] += 1

            # 移出視窗最左邊的字元
            left_char = s[right - len_p] # left_char = s[0]
            window[left_char] -= 1

            # Counter 會留下 0，要刪掉比較乾淨
            if window[left_char] == 0:   
                del window[left_char]

            # 如果視窗頻率和 p 相同，就找到 anagram
            if window == p_count:
                res.append(right - len_p + 1) # res = 2-2+1

        print(res)
        return res

s = "abab"
p = "ab"
sol = Solution()
sol.findAnagrams(s,p)
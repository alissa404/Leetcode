# anagram 要考慮 string 中每個 char 的出現次數，不考慮順序
# 所以不能用 set 因為set 沒有考慮到 有幾次，要使用 Counter 

from collections import Counter

class Solution:
# 解法一
    def isAnagram_2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    

# 解法二
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - ord('a')] += 1
    for ch in t:
        cnt[ord(ch) - ord('a')] -= 1

    return all(x == 0 for x in cnt)  # all() =「全部都要成立」

s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s,t))
# print(sol.isAnagram_2(s,t))
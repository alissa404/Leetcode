# hash map

#字母法
from collections import defaultdict

class Solution:
    def groupAnagrams_a(self, strs: List[str]) -> List[List[str]]:     
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            print(count)
            key = tuple(count)   # list 不能當 key，要轉 tuple
            res[key].append(s)

        return list(res.values())

# 時間 O(n · k)
# 空間 O(n)


##########################################################################

# 排序法
    def groupAnagrams_b(self, strs: List[str]) -> List[List[str]]:                
        res = defaultdict(list)
        for i in strs:
            temp = "".join(sorted(i))
            res[temp].append(i)
            print(res)
            
        return list(res.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams_a(strs))
# print(sol.groupAnagrams_b(strs))

# 有 N 個字串
# k = 單一字串長度
# 時間 O(N · K log K)
# 排序每個字串  O(K log K)
# 空間 O(N · K)
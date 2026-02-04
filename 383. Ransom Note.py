from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        big = Counter(magazine) 
        small = Counter(ransomNote)

        return small <= big

# 假設 ransomNote 的長度為 n，magazine 的長度為 m
# time O(n+m)
# space O(1)
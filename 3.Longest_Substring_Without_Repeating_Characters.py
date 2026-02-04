from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = defaultdict(int) # 記錄目前 window 裡每個字元有幾個
        ans = 0
        
        for right, ch in enumerate(s):
            # 依序建立dict
            window[ch] += 1
            print(window)
            '''
            defaultdict(<class 'int'>, {'a': 1})
            defaultdict(<class 'int'>, {'a': 1, 'b': 1})
            defaultdict(<class 'int'>, {'a': 1, 'b': 1, 'c': 1})
            defaultdict(<class 'int'>, {'a': 2, 'b': 1, 'c': 1})
            '''

            # window[ch]的值有重複時 → 收縮最左邊的字
            while window[ch] > 1:
                window[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
    
# 時間：O(n)， 空間：O(k)
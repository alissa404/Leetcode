from collections import defaultdict
from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        # s1 比 s2 還長，不可能是子排列
        if len1 > len2:
            return False

        need = defaultdict(int)   # 記錄 s1 每個字元的頻率
        window = defaultdict(int) # 記錄目前 window 裡每個字元有幾個

        # 建立 need 頻率表
        for ch in s1:
            need[ch] += 1

        # 先把 s2 的前 len1 個字元放進 window（第一個視窗）
        for i in range(len1):
            window[s2[i]] += 1

        # 如果一開始就一樣，直接 True
        if window == need:
            return True

        # 開始滑動視窗：右邊加一個字元，左邊移除一個字元
        for right in range(len1, len2):
            in_char = s2[right]           # 新進來的字元
            window[in_char] += 1

            out_char = s2[right - len1]   # 被移出視窗的字元
            window[out_char] -= 1        # 從window dict 中刪除了最左邊的字元
            
            if window[out_char] == 0:
                del window[out_char]      # 清掉window dict 裡面 value=0 的字元

            # 每滑動一次都檢查目前這個長度 len1 的 window
            if window == need:
                return True

        return False
    
# 時間：O(n)， 空間：O(k)
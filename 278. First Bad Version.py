def isBadVersion(version: int, bad: int) -> bool:
    if version >= bad:
        return True
    else: return False

class Solution:
    def firstBadVersion(self, n: int, bad) -> int:
        left = 1
        right = n
        
        # 使用二分搜尋
        while left < right:
            mid = (left + right) // 2   # 一定要括號! 不然會先乘除後加減
            
            if isBadVersion(mid,bad):
                # 如果 mid 壞了，代表「第一個壞的」在 mid 或 mid 的左邊
                right = mid
            else:
                # 如果 mid 沒壞，代表「第一個壞的」一定在 mid 的右邊
                left = mid + 1
        
        # 最後 left 和 right 會重合，指向第一個壞掉的版本
        return left

n= 5
bad = 4
print(Solution().firstBadVersion(n,bad))

# time : O(logn)
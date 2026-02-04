# 已經排序好的陣列 適合用雙指標
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # 找到中間點
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # 找到了，回傳索引
            elif nums[mid] < target:
                left = mid + 1  # 目標在右半邊，左邊界往右跳
            else:
                right = mid - 1 # 目標在左半邊，右邊界往左跳
                
        return -1

# 時間 O(log n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 排序 O(nlogn)
        nums.sort()
        res = []
        n = len(nums)

        # 外層 for i 迴圈跑了n 次
        for i in range(n-2):

            # 如果排序後最左邊第一個值都不是負數，代表沒有負數，總和不可能相加為 0
            if nums[i] > 0: break

            # 去重 避免第一個數重複（同樣的 nums[i] 只處理一次）
            if i > 0 and nums[i] == nums[i - 1]: continue

            left = i+1 # 從nums[i] 下一個則為 nums[left]
            right = n-1 # 最右邊的值


            # 從左到右走過一次陣列，所以是 n 次
            while left < right:
                sums = nums[left] + nums[i] + nums[right]

                if sums == 0:
                    # 要加中括號 才能append
                    res.append([nums[i], nums[left], nums[right]])

                    # 去重 左側重複值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 去重 右側重複值
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    right -= 1
                    left += 1

                elif sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
    
        return res


nums = [-2, 0, 0, 2, 2]
solver = Solution()
print(solver.threeSum(nums))

# 時間：O(n^2)， 空間：O(1)
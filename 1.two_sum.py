class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, x in enumerate(nums):
            temp = target - x

            if temp in hashmap:
                return [hashmap[temp], index] # hashmap[key] 就會得到 value
            
            # 將 x 當作 key, index 當作 value 存入dict(hashmap)中
            hashmap[x] = index
            print(hashmap)

        return
    
# 時間：O(n)， 空間：O(n)

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))
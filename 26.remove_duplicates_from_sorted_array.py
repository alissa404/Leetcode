class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        index = 0
        for i in range(len(nums)):
            if (i == 0 or nums[i] != nums[i-1]):
                nums[index] = nums[i]
                index += 1
    
        return index
    
    # 時間複雜度：O(n)（必須線性掃過整個陣列，已是最優）空間複雜度：O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1. 準備一個空的記憶本
        seen = set()
        
        # 2. 開始一個一個看數字
        for i in nums:
            # 3. 檢查：這個數字是不是已經在記憶本裡了？
            if i in seen:
                return True  # 既然看過了，代表有重複，馬上回傳 True
            
            # 4. 沒看過的話，就把這個數字記在記憶本裡
            seen.add(i)
            
        # 5. 如果全部跑完都沒遇到重複，回傳 False
        return False


nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))

# time O(n)
# space O(n)
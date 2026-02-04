# 由於是 subarray 所以不能重新排序，有固定順序

# prefix sum -> 從頭開始連續的總值

# 用hashmap 來記錄

# 去檢查 prefix_sum - k 有沒有之前存在過 hashmap 當中

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        res = 0
        prefix_sum = 0
        
        # prefix_count 存的是：某個前綴和出現了幾次
        prefix_count = defaultdict(int) 
        
        # 【重要】初始化：前綴和為 0 的情況出現過 1 次
        prefix_count[0] = 1

        for i in nums:
            prefix_sum += i
            
            # 去檢查 prefix_sum - k 有沒有之前存在過 dict 當中
            target = prefix_sum - k
            if target in prefix_count:
                res += prefix_count[target]
                '''
                為什麼要 res += prefix_count[target] 而不是 res += 1？
                
                因為有「兩個過去的時間點」都能讓你現在的總和變成 3
                路徑 A：從「最初的 0」到現在 子陣列是 [1, -1, 3]，總和為 3。
                路徑 B：從「第二個 0」到現在 子陣列是 [3]，總和為 3。
                如果不寫 += prefix_count[target]，你就會漏掉其中一種組合！
                能處理包含 0 或正負抵銷的情況
                '''
            
            # 紀錄當前的前綴和 的出現次數
            else: prefix_count[prefix_sum] += 1
            
        return res
            
nums = [1, -1, 3]
k = 3
print('ans:',Solution().subarraySum(nums,k))

# 時間複雜度是 O(n)，空間複雜度也是 O(n)
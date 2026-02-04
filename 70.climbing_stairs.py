# DP 動態規劃 本質就是 Fibonacci 數列

class Solution:
    def climbStairs(self, n: int) -> int:
        pre,  cur = 1, 1
        for i in range(1,n):
            pre, cur = cur, pre+cur

        '''
        pre = dp[i-2]
        cur = dp[i-1]
        '''

        print(cur)
        return  cur
    
n = 3
Solution().climbStairs(n)

'''
output = 3
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# 時間 O(n)
# 空間 O(1) 
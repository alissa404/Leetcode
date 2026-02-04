# 單調堆疊（Monotonic Stack）

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)  # [0,0,0...]

        for i, t in enumerate(temperatures): # i=0, t=30 # i=1, t=40

            # while current temp is higher, resolve previous colder days
            while stack and temperatures[stack[-1]] < t:  # stack[-1] 表示 stack 頂端那一天
                j = stack.pop() # 當 i=1, t=40, j = 0
                ans[j] = i-j # ans[0] = 1-0
            stack.append(i) 
            # 當i=0, t=30 的時候，跳過while 直接stack = [0]
        
        return ans

temperatures = [30,40,50,60]
sol = Solution()
print(sol.dailyTemperatures(temperatures))

# 時間複雜度 O(n)，空間複雜度：O(n)
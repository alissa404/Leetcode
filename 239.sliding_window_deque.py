from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # store indices, nums[dq] is decreasing
        ans = []

        for i, x in enumerate(nums):
            # 1) remove indices out of window (expired)
            left = i - k + 1
            if dq and dq[0] < left:
                dq.popleft()

            # 2) maintain decreasing order: pop smaller values from the back
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            # 3) push current index
            dq.append(i)

            # 4) record answer once first window is formed
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans

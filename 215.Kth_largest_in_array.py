# divide and conquer
# quick select 只做 partition sort 比 quick sort and merge sort 還要快
# 但有大量重複值，用2way 會錯，只能用3way QuickSelect

import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target_index = n - k  # kth largest 
        left, right = 0, n - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]
            lt, gt = self.partition3(nums, left, right, pivot)
            # nums[left..lt-1] < pivot
            # nums[lt..gt]     == pivot
            # nums[gt+1..right]> pivot

            if target_index < lt:
                right = lt - 1
            elif target_index > gt:
                left = gt + 1
            else:
                return nums[target_index]

        raise ValueError("Invalid input")

    def partition3(self, nums: List[int], left: int, right: int, pivot: int):
        lt, i, gt = left, left, right
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt -= 1
            else:
                i += 1
        return lt, gt

'''
時間平均：O(n)
最壞：O(n²)

空間 : O(1)
'''
#############################################################################

# Min Heap

import heapq
from typing import List

class Solution:
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)  # 移除最小的，讓堆保持 k 個最大值
        return heap[0]

'''
時間：O(n log k)
空間：O(k)
'''

nums = [3,2,1,5,6,4]
k = 2
# print(Solution().findKthLargest(nums,k))
print(Solution().findKthLargest_heap(nums,k))
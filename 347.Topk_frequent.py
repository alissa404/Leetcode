# 從所有元素中，找出「出現次數最多的 K 個」
# min-heap

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) 
        heap = []  # 存 (count, num)

        for num, cnt in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            else: 
                # len(heap) > k  超過 最多可存取 k 個最大值了
                # heap[0] 是目前 top k 裡「最小頻率」的
                if cnt > heap[0][0]:
                    heapq.heapreplace(heap, (cnt, num))  

        return [num for (cnt, num) in heap]

nums = [1,1,1,2,2,3,4]
k = 2
print(Solution().topKFrequent(nums, k))

# 時間：O(n + m log k)（n=nums 長度，m=不同元素數量，m≤n）
# 空間：O(m + k)（Counter + heap）
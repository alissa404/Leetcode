# Max Heap 找 kth 最小值(最短距離)

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        if n == k:
            return points
        
        # heap 存 (-distance, x, y)
        # 取負數只是因為 Python heapq 只支援 min-heap
        heap = []
        for x, y in points:
            d = x*x + y*y

            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y)) #-18, -26, -20
            else:
                # heap[0] 是目前「最遠」的那個（因為 dist 取負，最小的負值 = 最大的 dist）
                if d < -heap[0][0]:  # 新點距離 d < 目前最遠的距離 -heap[0][0]
                    # 20 < 26
                    heapq.heapreplace(heap, (-d, x, y))  # pop + push 的合併操作

        return [[x, y] for (_, x, y) in heap]

points = [[3,3],[5,-1],[-2,4]] 
k = 2
print(Solution().kClosest(points,k))

'''
- Time`O(n log k)`
- Space`O(k)`
'''
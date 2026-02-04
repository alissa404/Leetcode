class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        while m>0 and n>0 :         
            # nums1[m-1] 表nums1中最大的 一個非0的值
            # nums1最大值大於nums2
            if nums1[m-1] > nums2[n-1]:
                #將nums1最大值移到最後面
                nums1[m+n-1] = nums1[m-1]        
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1] 
                n-=1

        # m or n = 0
        nums1[:n] = nums2[:n]
      
        return

# 時間：O(m + n) 空間：O(1)
# https://leetcode.com/problems/merge-sorted-array/description/
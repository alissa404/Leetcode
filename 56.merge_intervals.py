class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        # only one set
        if len(intervals)<2:
            return intervals
            
        res = []
        #先排好全部list的順序
        intervals = sorted(intervals) 
        
        for i in intervals:            
            # i[0] 表示每個list中第一個值
            # i[1] 表示每個list中第二個值
            # res[-1][1] 表示前一個已排好的小list         
            if len(res)==0 or i[0]>res[-1][1]:
                res.append(i)
            else:
                # 比較第二個值，較大的留下
                res[-1][1] = max(res[-1][1], i[1])
                
        return res
    
# 時間複雜度 : O(n log n) 空間複雜度：O(n)
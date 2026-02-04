class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I":1,"V":5, "X":10,"L":50,"C":100,"D":500 ,"M":1000}
        pre, total = 0, 0
        # pre 表示前一個羅馬字
        
        for i in s:
            temp = dict1[i]
            total += temp
            
            # IX 後大於前
            if temp > pre:  
                total -= pre*2  #減掉x2 是因為我下一段不管怎樣會先加進去了 所以減兩次
            pre = temp

        return total
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False
        if len(s)==0: return True  
        
        stack = []
        for i in s:
            if i =="(" or i =="[" or i =="{":
                stack.append(i)
            
            else:
                if len(stack)==0:
                    return False
                
                else:
                    temp = stack.pop()
                    # temp 是 i 的前一個 tuple
                    if i ==")" and temp != "(":
                            return False
                    elif i =="]" and temp != "[":
                            return False
                    elif i =="}"  and temp != "{":
                            return False

        # 都是正確配對的情況，stack 配對完畢 
        if len(stack)==0:
            return True
        else:
            return False
        
# 時間:O(n) 空間:O(n)
#雙指標，一左一右往中間走

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 只留英文字母 並轉小寫
        s = "".join(char.lower() for char in s if char.isalnum())
        # Join every lowered char from s only if the char is alphanumeric. 
        # 結合 每個 變小寫的字元 來自 s 只要 該字元是英數 
        n = len(s)
        
        # index
        left = 0
        right = n-1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
                
        return True
    
s = "aba"
print(Solution().isPalindrome(s))

# 時間：O(n)， 空間：O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # mismatch 時，試試看刪左或刪右
                return (self.isPlainPalindrome(s, left + 1, right) or
                        self.isPlainPalindrome(s, left, right - 1))

        return True

    def isPlainPalindrome(self, s: str, left: int, right: int) -> bool:
        # 這裡就只是「單純回文檢查」，不再允許刪字元
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# 時間：O(n)， 空間：O(1)
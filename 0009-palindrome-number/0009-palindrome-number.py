class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True

        return str(x) == str(x)[::-1]
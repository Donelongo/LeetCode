class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        reverse_str = num_str[::-1]
        return num_str == reverse_str
        
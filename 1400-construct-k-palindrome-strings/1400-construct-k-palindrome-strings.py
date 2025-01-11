class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If we need more palindromes than the number of characters, it's impossible
        if k > len(s):
            return False
        
        # Count the frequency of each character in the string
        freq = Counter(s)
        
        # Count the number of characters with an odd frequency
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)
        
        # We can construct k palindromes if the odd count is <= k
        return odd_count <= k     
from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            freq = Counter(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])
        
        result = []
        for word in words1:
            freq = Counter(word)
            is_universal = True
            for char in max_freq:
                if freq[char] < max_freq[char]:
                    is_universal = False
                    break
            if is_universal:
                result.append(word)

        return result


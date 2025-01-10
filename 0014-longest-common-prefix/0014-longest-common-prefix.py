class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            current_char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != current_char:
                    return strs[0][:i]
        return strs[0][:min_length]
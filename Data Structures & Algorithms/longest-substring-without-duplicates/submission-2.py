class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i= 0
        char = set()
        max_len =0
        for j in range(len(s)):
            while s[j] in char:
                char.remove(s[i])
                i += 1
            char.add(s[j])
            max_len =max(max_len,j-i+1)
        return max_len         
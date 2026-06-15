class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        left =strs[0]
        right =strs[-1]
        i = 0
        while i < len(left) and i< len(right)and left[i] == right[i]:
            i += 1
        return left[:i]
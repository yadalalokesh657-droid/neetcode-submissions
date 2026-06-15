class Solution:
    def isPalindrome(self, s: str) -> bool:
        same_s ="".join(c.lower()for c in s if c.isalnum())
        left = 0
        right = len(same_s)-1
        while left < right:
            if same_s[left] != same_s[right]:
                return False
            left += 1
            right -= 1
        return True

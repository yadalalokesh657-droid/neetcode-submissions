class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, r):
            while l < r:
                if s[l].lower()!= s[r].lower():
                  return False
                            
                l += 1
                r -= 1
            return True
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].lower()!= s[right].lower():
                                                                                                                                                                # NO colon here. And call check, not palindrome
                return check(left+1, right) or check(left, right-1)
            left += 1
            right -= 1
        return True
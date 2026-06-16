class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for d in nums:
            if d in seen:
                return True
            seen.add(d)
        return False
        
        
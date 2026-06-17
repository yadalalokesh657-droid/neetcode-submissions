class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        window ={}
        required =len(need)
        formed = 0
        min_len = float('inf')
        result =""
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0)+1
            if char in need and window[char] == need[char]:
                formed += 1
            while formed == required:
                if right -left+1 < min_len:
                    min_len = right-left+1
                    result = s[left:right+1]
            
                
                if s[left] in need and window[s[left]] == need[s[left]]:
                    formed -= 1
                window[s[left]] -= 1
                left += 1
    
                
        return result
        
        
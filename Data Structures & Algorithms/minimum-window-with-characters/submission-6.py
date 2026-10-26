class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {},{}
        for c in t:
            countT[c] = countT.get(c,0)+1
        left = 0
        have, need = 0,len(countT)
        res, reslen = [-1,-1] , float("inf")
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0)+1
            if  c in countT and window[c] == countT[c]:
                have += 1
                #update the function 
            while have == need:
                if (right-left+1)< reslen :
                    res = [left,right]
                    reslen = right - left +1
                    #pop from left window
                window [s[left]] -= 1
                if s[left] in countT and window [s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left,right = res
        return s[left:right+1] if reslen !=  float("inf") else ""               






        
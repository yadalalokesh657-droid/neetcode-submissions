class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for val in s:
            if val in "([{":
                stack.append(val)
            else:
                if not stack:
                    return False
                if stack.pop() != mp[val]:
                    return False
        return not stack

        
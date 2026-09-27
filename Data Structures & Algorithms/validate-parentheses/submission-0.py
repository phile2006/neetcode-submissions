class Solution:
    def isValid(self, s: str) -> bool:
        counter_part = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in s:
            if i in counter_part:
                if not stack:
                    return False
                if stack.pop() != counter_part[i]:
                    return False               
            else:
                stack.append(i)
            
        return True if not stack else False
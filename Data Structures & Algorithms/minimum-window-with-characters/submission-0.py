class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_T = {}
        window = {}
        for x in t:
            count_T[x] = count_T.get(x, 0) + 1
        
        have, need , result, resultLen = 0, len(count_T), [-1, -1], float("infinity")
        left = 0


        for right in range(len(s)):
            character = s[right]
            window[character] = window.get(character, 0) + 1

            if character in count_T and window[character] == count_T[character]:
                have += 1

            while have == need:
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = (right - left + 1)
                window[s[left]] -= 1
                if s[left] in count_T and window[s[left]] < count_T[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left:right + 1] if resultLen != float("infinity") else ""



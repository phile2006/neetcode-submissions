class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        window = {}
        need = {}

        if n > len(s2): 
            return False

        for i in range(n):
            need[s1[i]] = need.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        if window == need:
            return True
        
        for right in range(n, len(s2)):
            character_in = s2[right]
            window[character_in] = window.get(character_in, 0) + 1

            character_out = s2[right - n]
            window[character_out] -= 1
            if window[character_out] == 0:
                del window[character_out]

            if window == need: 
                return True
        return False

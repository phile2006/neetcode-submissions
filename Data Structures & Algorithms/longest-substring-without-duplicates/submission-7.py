class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found_characters = []
        max_count  = 0

        for i in range(len(s)):
            if s[i] in found_characters:
                del found_characters[0:found_characters.index(s[i]) + 1]
                found_characters.append(s[i])

                if max_count < len(found_characters):
                    max_count = len(found_characters)
            else:
                found_characters.append(s[i])

                if max_count < len(found_characters):
                    max_count = len(found_characters)

        return max_count
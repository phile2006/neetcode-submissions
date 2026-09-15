class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        cleaned = []
        for character in s_lower:
            if character.isalnum():
                cleaned.append(character)

        reverse_characters = cleaned[::-1]
        
        return cleaned == reverse_characters
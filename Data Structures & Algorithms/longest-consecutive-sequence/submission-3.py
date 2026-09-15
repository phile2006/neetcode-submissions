class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0

        for i in num_set:
            if i - 1 not in num_set:
                current = i
                current_streak = 1

                while current + 1 in num_set:
                    current += 1
                    current_streak += 1
                
                streak = max(streak, current_streak)
        return streak
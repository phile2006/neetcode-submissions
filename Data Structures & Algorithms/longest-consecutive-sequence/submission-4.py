class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0

        for i in num_set:
            if i - 1 not in num_set:
                current = i

                while current in num_set:
                    current += 1
                
                current_streak = current - i
                if current_streak > streak:
                    streak = current_streak
        return streak
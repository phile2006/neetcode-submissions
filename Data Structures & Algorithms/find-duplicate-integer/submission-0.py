class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts, key = counts.get)
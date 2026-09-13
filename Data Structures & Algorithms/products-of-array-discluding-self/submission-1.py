class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        suf = 1
        for i in range(1, n):
            out[i] = out[i-1] * nums[i-1]
        for i in range(n-1, -1, -1):
            out[i] *= suf
            suf *= nums[i]
        return out
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        curr_sum = 0

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            elif i >= len(nums) or curr_sum > target:
                return

            subset.append(nums[i])
            curr_sum += nums[i]
            dfs(i, curr_sum)
            subset.pop()
            curr_sum -= nums[i]
            dfs(i + 1, curr_sum)
        dfs(0,curr_sum)
        return res
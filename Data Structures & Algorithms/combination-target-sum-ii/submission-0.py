class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        c_sum = 0
        candidates.sort()

        def dfs(i, c_sum): 
            if c_sum == target and subset not in res:
                res.append(subset.copy())
                return

            elif i >= len(candidates) or c_sum > target:
                return
            subset.append(candidates[i])
            dfs(i + 1, c_sum + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, c_sum)

        dfs(0, c_sum)
        return res

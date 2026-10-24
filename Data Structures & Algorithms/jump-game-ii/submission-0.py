import heapq
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        ind = 0
        count = 0
        while ind <= len(nums) - 1:
            if ind + nums[ind] >= len(nums) -1:
                count += 1
                return count

            max_heap = []
            heapq.heapify(max_heap)
            for i in range(ind, ind + nums[ind] + 1):
                heapq.heappush(max_heap, (-(i + nums[i]), i) )
            neg_reach , ind = heapq.heappop(max_heap)
            count += 1
        return count





class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [-i for i in nums]
        heap = heapq.heapify(num)
        out = 0

        for i in range(k):
            out = -heapq.heappop(num)
        return out

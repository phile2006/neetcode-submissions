import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            v1 = -heapq.heappop(heap)
            v2 = -heapq.heappop(heap)
            if v1 > v2:
                heapq.heappush(heap, -(v1 - v2))
        
        return -heap[0] if heap else 0
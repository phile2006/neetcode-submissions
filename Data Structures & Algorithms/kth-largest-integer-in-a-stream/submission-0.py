import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        num = self.nums.copy()
        heap = heapq.heapify(num)
        #for i in self.num:
        #    heapq.heappush(heap, -i)
        self.nums.append(val)
        heapq.heappush(num, val)
        maxV = heapq.nlargest(self.k,num)
        
        return maxV[len(maxV) - 1]

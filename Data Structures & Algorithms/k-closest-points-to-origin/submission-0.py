import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for i in range(len(points)):
            dist = math.sqrt((0 - points[i][0]) ** 2 + (0 - points[i][1])** 2)
            heapq.heappush(heap, (dist,points[i][0],points[i][1]))     
               
        out = []
        for j in range(k):
            dis, x, y = heapq.heappop(heap)
            out.append([x,y])
        
        return out
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals is None:
            return None
        
        elif len(intervals) == 1:
            return [intervals[0]]
        intervals.sort()


        start = min(intervals[0][0], intervals[1][0])#1
        out = []
        highest_end_index = (intervals[0][1], 0)
        for i in range(1, len(intervals)):


            if highest_end_index[0] < intervals[i][0]:
                out.append([start,highest_end_index[0]])
                start = intervals[i][0]
                highest_end_index = 0,0

            if highest_end_index[0] < intervals[i][1]:
                highest_end_index = intervals[i][1], i
            


            if i == len(intervals) - 1:
                out.append([start, highest_end_index[0]])

        return out

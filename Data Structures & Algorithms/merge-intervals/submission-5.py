class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:      
        if len(intervals) == 1:
            return [intervals[0]]
        intervals.sort()


        start = intervals[0][0]
        out = []
        highest_end_index = intervals[0][1]
        for i in range(1, len(intervals)):


            if highest_end_index < intervals[i][0]:
                out.append([start,highest_end_index])
                start = intervals[i][0]

            if highest_end_index < intervals[i][1]:
                highest_end_index = intervals[i][1]
            


            if i == len(intervals) - 1:
                out.append([start, highest_end_index])

        return out

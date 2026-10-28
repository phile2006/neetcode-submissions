class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict()

        for ind, st in enumerate(s):
            last[st] = ind
        
        out = []
        l = 0
        while l < len(s):
            start = s[l]
            start_ind = l
            end = last[start]

            while l <= end:

                end = max(last[s[l]], end)
                l += 1
            out.append(end - start_ind + 1)
        return out



        
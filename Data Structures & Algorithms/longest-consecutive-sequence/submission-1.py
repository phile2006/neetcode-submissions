class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numss = sorted(nums)
        no_duplicate = list(dict.fromkeys(numss))
        counts = [] #multiple counts to later sort list and take highest value
        #2,3,4,5,10,20
        count = 1
        for i in range(len(no_duplicate)-1):
            if no_duplicate[i+1] - no_duplicate[i] == 1:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts.append(count)
        return max(counts)
            

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        val = True
        gap = 0
        for i in nums[-2::-1]: # start at the index before last
            if i == 0:
                gap += 1
                val = False
            elif gap < i:
                gap = 0
                val = True
            elif i <= gap:
                gap += 1 # since the value before cannot jumo over gap we need a number able to jump over the number

        return val

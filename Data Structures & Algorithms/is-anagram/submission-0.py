class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        counts_hashmap = {}
        
        for x in s:
            counts_hashmap[x] = counts_hashmap.get(x, 0) + 1
        
        for x in t:
            counts_hashmap[x] = counts_hashmap.get(x, 0) - 1

        for count in counts_hashmap.values():
            if count != 0:
                return False
                
        return True

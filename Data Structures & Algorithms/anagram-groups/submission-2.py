class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for x in strs:
            res["".join(sorted(x))].append(x)
        return list(res.values())
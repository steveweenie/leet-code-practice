class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            h[key].append(s)
        
        return list(h.values())
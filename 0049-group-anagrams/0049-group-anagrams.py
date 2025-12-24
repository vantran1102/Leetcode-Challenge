class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for w in strs:
            key = "".join(sorted(w.lower()))
            if key not in groups:
                groups[key]=[]
            groups[key].append(w)
        return list(groups.values())
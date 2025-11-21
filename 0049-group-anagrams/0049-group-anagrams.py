class Solution(object):
    def groupAnagrams(self, strs):
        anagram_group={}
        for w in strs:
            key = "".join(sorted(w))
            if key not in anagram_group:
                anagram_group[key]=[]
            anagram_group[key].append(w)
        return list(anagram_group.values())
        
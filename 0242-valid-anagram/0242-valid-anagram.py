class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sortedCharacter = sorted(s)
        s_sorted = "".join(s_sortedCharacter)
        t_sortedCharacter = sorted(t)
        t_sorted = "".join(t_sortedCharacter)
        if s_sorted == t_sorted:
            return True
        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1,count2={},{}
        l=0
        k = len(s1)
        if len(s1)>len(s2):
            return False
        for r1 in range(len(s1)):
                count1[s1[r1]] = 1 + count1.get(s1[r1],0)
        for r2 in range(len(s2)):
            count2[s2[r2]] = 1 + count2.get(s2[r2],0)
            if r2-l+1 > k:
                count2[s2[l]]-=1
                if count2[s2[l]]==0:
                    count2.pop(s2[l])
                l+=1
            if count1 == count2:
                return True
        return False



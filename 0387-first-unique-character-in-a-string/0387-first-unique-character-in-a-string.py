class Solution(object):
    def firstUniqChar(self, s):
        seen={}
        for l in s:
            if l in seen:
                seen[l]+=1
            else:
                seen[l]=1
        non_dup = []
        for ch,count in enumerate(s):
            if seen[count] == 1:
                return ch
        return -1
        
class Solution(object):
    def findDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        duplicate=0
        for value, count in seen.items():
            if count > 1:
                duplicate+=value
        return duplicate
        
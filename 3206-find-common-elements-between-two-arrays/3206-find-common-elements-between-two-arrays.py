class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        hash1={}
        hash2={}
        count1=0
        count2=0
        for i in nums1:
            hash1[i]= True
        for j in nums2:
            hash2[j]= True
        for i in nums1:
            if i in hash2:
                count1 += 1
        for j in nums2:
            if j in hash1:
                count2 += 1
        return [count1,count2]
        
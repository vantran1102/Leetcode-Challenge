class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        #----------Solution1-----------
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
        #-------------Solution2----------
        # set1 = set(nums1)
        # set2 = set(nums2)

        # count1 = sum(1 for x in nums1 if x in set2)
        # count2 = sum(1 for y in nums2 if y in set1)

        # return [count1, count2]
        
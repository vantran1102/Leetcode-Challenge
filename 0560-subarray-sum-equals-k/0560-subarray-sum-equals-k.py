class Solution(object):
    def subarraySum(self, nums, k):
        total = 0
        dict = {}
        counter = 0
        for num in range(len(nums)):
            total += nums[num]
            if total == k:
                counter += 1
            if (total - k) in dict:
                counter += dict[total - k]
            if total in dict:
                dict[total]+=1
            else:
                dict[total]=1
        return counter
        


        
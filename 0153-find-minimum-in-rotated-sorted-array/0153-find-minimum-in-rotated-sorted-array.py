class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        result = nums[0]
        while l <= r:
            if nums[l]<nums[r]:
                result = min(result,nums[l])
            mid = (l+r)//2
            result = min(result,nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else: #nums[mid]<nums[r]
                r = mid - 1
        return result
                

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        total_ones = nums.count(1)
        l=0
        window_ones = max_window_ones = 0 #number of 1 currently inside window
        for r in range(2*N): #2*N since array treated as circular 
            if nums[r%N]==1:
                window_ones+=1
            if r - l + 1 > total_ones:
                window_ones -= nums[l%N]
                l+=1
            max_window_ones = max(window_ones, max_window_ones)
        return total_ones - max_window_ones

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            left_arr = nums[0 : index]
            right_arr = nums[index+1 : ]
            if (target-num) in left_arr:
                return [left_arr.index(target-num),index]
            elif (target-num) in right_arr:
                return [index,right_arr.index(target-num)+index+1]
        return []

        
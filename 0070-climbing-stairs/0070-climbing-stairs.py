class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1
        for temp in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        
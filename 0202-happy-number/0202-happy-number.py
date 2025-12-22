class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def square_number(n):
            sum = 0
            while n>0:
                digit = n%10
                sum += digit*digit
                n = n//10
            return sum
        while n!=1 and n not in seen:
            seen.add(n)
            n = square_number(n)
        return n==1
        
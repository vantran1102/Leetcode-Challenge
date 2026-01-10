class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hour_needed(k):
            total = 0
            for p in piles:
                total += (p+k-1)//k
            return total
        lo,hi = 1, max(piles)
        while lo <= hi:
            mid = (lo+hi)//2
            hour = hour_needed(mid)
            if hour <= h:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

import heapq
class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []
    def addNum(self, num: int) -> None:
        if not self.first_half or num <= -self.first_half[0]:
            heapq.heappush(self.first_half, -num)
        else:
            heapq.heappush(self.second_half, num)
        if len(self.first_half) > len(self.second_half) + 1:
            heapq.heappush(self.second_half, -heapq.heappop(self.first_half))
        elif len(self.second_half) > len(self.first_half)+1:
            heapq.heappush(self.first_half,-heapq.heappop(self.second_half))


    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half):
            median = (-self.first_half[0]+self.second_half[0]) / 2
        elif len(self.first_half) > len(self.second_half):
            median = -self.first_half[0]
        else:
            median = self.second_half[0]
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap=[]
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=0
            freq[num]+=1
        result=[]
        for num,count in freq.items():
            heapq.heappush(max_heap,(-count,num))
        while k > 0:
            negative_count, num = heapq.heappop(max_heap)
            result.append(num)
            k-=1
        return result
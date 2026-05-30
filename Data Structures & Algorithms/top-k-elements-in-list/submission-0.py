from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        print(freq)
        l=heapq.nlargest(k,freq.items(),key=lambda x:x[1])
        return [x[0] for x in l]


        
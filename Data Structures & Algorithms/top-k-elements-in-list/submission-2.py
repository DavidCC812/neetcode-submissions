from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num, frequency in count.items():
            heapq.heappush(heap, (frequency, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for frequency, num in heap]

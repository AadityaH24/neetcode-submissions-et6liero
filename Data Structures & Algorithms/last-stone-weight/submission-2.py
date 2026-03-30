import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert to a max-heap by negating values
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # heaviest
            x = -heapq.heappop(heap)  # second heaviest

            if x != y:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0
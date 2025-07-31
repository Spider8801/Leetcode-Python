import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heap=[]

    for num in nums:
        if len(heap)<k:
            heapq.heappush(heap,num)

        elif num>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,num)

    return heap[0]
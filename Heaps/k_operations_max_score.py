import heapq
import math
from typing import List


def maxKelements( nums: List[int], k: int) -> int:
    max_heap=[]
    max_sum=0

    for num in nums:
        heapq.heappush(max_heap,-num)

    while k>0:
        k-=1
        max_element=-heapq.heappop(max_heap)
        max_sum+=max_element
        heapq.heappush(max_heap,-math.ceil(max_element/3))
    return max_sum
    
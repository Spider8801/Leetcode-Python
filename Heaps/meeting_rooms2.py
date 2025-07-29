import heapq
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    
    intervals.sort()

    min_heap = []

    for interval in intervals:
        start, end = interval

        if min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        
        heapq.heappush(min_heap, end)
    
    return len(min_heap)
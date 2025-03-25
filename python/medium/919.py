"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # starts = [interval.start for interval in intervals]
        # ends = [interval.end for interval in intervals]

        # starts.sort()
        # ends.sort()

        
        # i = j = 0
        # ans = min_days = 0
        # while(i < len(starts)):
        #     if starts[i] < ends[j]:
        #         i += 1
        #         min_days += 1
        #     else:
        #         j += 1
        #         min_days -= 1
        #     ans = max(ans, min_days)
        # return ans

        # Heap approach

        intervals.sort(key = lambda i: i.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval.end)
        
        return len(min_heap)
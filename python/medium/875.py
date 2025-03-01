class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def banana_check(speed):
            hours = 0
            for pile in piles:
                hours += ceil(pile / speed)
            
            return hours <= h

        left = 1
        right = max(piles)
        min_speed = right

        while left <= right:
            mid = left + (right - left) // 2

            if banana_check(mid):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1

        return min_speed
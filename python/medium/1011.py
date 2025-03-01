class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            days_temp = 1
            curr_capacity = 0
            for weight in weights:
                curr_capacity += weight
                if curr_capacity > capacity:
                    days_temp += 1
                    curr_capacity = weight
            return days_temp <= days
        
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2

            if canShip(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
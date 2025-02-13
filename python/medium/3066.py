class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        num_operations = 0
        heapq.heapify(nums)
        while nums[0] < k and len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, (min(x, y) * 2 + max(x, y)))
            num_operations += 1
        
        return num_operations
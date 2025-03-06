class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        curr_sum = 0
        ans = len(nums) + 1
        
        for j in range(len(nums)):
            curr_sum += nums[j]

            while curr_sum >= target:
                ans = min(j-i+1, ans)
                curr_sum -= nums[i]
                i += 1
        
        return ans if ans < len(nums) + 1 else 0
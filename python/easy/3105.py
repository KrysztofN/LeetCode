class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1

        inc_count = 1
        dec_count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_count += 1
                dec_count = 1

            elif nums[i] < nums[i-1]:
                dec_count += 1
                inc_count = 1            
            else:
                inc_count = 1
                dec_count = 1

            ans = max(ans, inc_count)
            ans = max(ans, dec_count)
        
        return ans
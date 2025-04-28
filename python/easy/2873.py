class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = 0
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                curr_val = 0
                for k in range(j + 1, len(nums)):
                    curr_val = (nums[i] - nums[j]) * nums[k]
                    max_triplet = max(max_triplet, curr_val)

        return max_triplet 
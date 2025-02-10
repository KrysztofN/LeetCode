class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # brute force O(n^2)
        # bad_pairs = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if j - i != nums[j] - nums[i]:
        #             bad_pairs += 1
        # return bad_pairs

        # Optimized

        totalpair = 0
        goodpair = 0
        count = defaultdict(int)
        for i in range(len(nums)):
            totalpair += i
            goodpair += count[nums[i] - i]
            count[nums[i] - i] += 1

        return totalpair - goodpair
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        ans = 0

        productSum = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] != nums[j]:
                    productSum[nums[i] * nums[j]] += 1
        
        for key, values in productSum.items():
            if values >= 2:
                ans += comb(values, 2) * 8
        
        return ans

                
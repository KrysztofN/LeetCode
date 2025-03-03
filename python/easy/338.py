class Solution:
    def countBits(self, n: int) -> List[int]:
        # def set_bits(num):
        #     set_bits = 0
        #     while num:
        #         set_bits += num & 1
        #         num >>= 1
        #     return set_bits

        # ans = []
        # for i in range(n+1):
        #     ans.append(set_bits(i))
        # return ans
        
        # Optimized
        ans = [0] * (n + 1)
        sub = 1

        for i in range(1, n +1):
            if sub * 2 == i:
                sub = i
            ans[i] = ans[i - sub] + 1
        return ans    
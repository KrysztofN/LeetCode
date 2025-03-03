class Solution:
    def hammingWeight(self, n: int) -> int:
        # set_bits = 0
        # while n:
        #     if n % 2 == 1:
        #         set_bits += 1
        #     n //= 2
        # return set_bits
        set_bits = 0
        while n:
            set_bits += n & 1
            n >>= 1
        return set_bits
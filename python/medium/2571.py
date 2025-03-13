class Solution:
    def minOperations(self, n: int) -> int:
        # 128 64 32 16 8 4 2 1
        #   0  0  1  0 1 1 1 0

        ans = 0
        while n:
            if n & 1:
                streak = 0
                while n and n & 1:
                    streak += 1
                    n >>= 1
                
                if streak == 1:
                    ans += 1
                else:
                    ans += 1
                    n |= 1
            else:
                n >>= 1
        return ans
      
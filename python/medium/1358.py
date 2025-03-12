class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # O(n^2)
        # ans = 0
        # for i in range(len(s)):
        #     a = 0
        #     b = 0
        #     c = 0
        #     for j in range(i, len(s)):
        #         if s[j] == "a":
        #             a = 1
        #         elif s[j] == "b":
        #             b = 1
        #         elif s[j] == "c":
        #             c = 1
        #         if a and b and c:
        #             ans += len(s) - j
        #             break
        # return ans

        # Optimized 2 pointer technique
        n = len(s)
        ans = 0
        freq = defaultdict(int)
        left, right = 0,0
        while right < n:
            freq[s[right]] += 1
            while freq["a"] > 0 and freq["b"] > 0 and freq["c"] > 0:
                ans += n - right
                freq[s[left]] -= 1
                left += 1
            right += 1
        return ans
        
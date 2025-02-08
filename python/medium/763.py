class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # O(n^2) approach
        # ans = []

        # min_r = 0
        # max_r = 0
        # curr_r = 0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         if s[i] == s[j]:
        #             curr_r = j
            
        #     max_r = max(max_r, curr_r)

        #     if(i == max_r):
        #         print(max_r)
        #         # partition
        #         ans.append(len(s[min_r:max_r+1]))
        #         curr_r = max_r+1
        #         min_r = curr_r
        
        # return ans

        # O(2*n) ~ O(n) approach
        ans = []
        table = {}
        for idx, val in enumerate(s):
            table[val] = idx
        
        max_idx = 0
        count = 0
        for i in range(len(s)):
            max_idx = max(max_idx, table[s[i]])
            count += 1
            
            if i == max_idx:
                ans.append(count)
                count = 0
        
        return ans

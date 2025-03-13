class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Not optimized
        # ans = 0
        # for query in queries:
        #     if sum(nums) == 0:
        #         break
        #     ans += 1
        #     for i in range(query[0], query[1]+1):
        #         if nums[i] < query[2]:
        #             nums[i] = 0
        #         else:
        #             nums[i] -= query[2] 

        # if sum(nums) == 0:
        #     return ans
        # else:
        #     return -1

        # Optimized diff array
        n = len(nums)
        diff = [0] * (n + 1)
        summ = 0
        pos = 0
        for i in range(n):
            while(summ + diff[i] < nums[i]):
                if pos == len(queries):
                    return -1
                
                l = queries[pos][0]
                r = queries[pos][1]
                v = queries[pos][2]
                pos += 1

                if(r < i): continue

                diff[max(l, i)] += v
                diff[r+1] -= v
            summ += diff[i]
        return pos
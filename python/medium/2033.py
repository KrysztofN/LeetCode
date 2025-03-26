class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        flattened_list = sorted([num for nums in grid for num in nums])
        mid = (len(flattened_list))//2
        target = flattened_list[mid]

        ans = 0
        for num in flattened_list:
            if (num - target) % x != 0:
                return -1
            ans += abs(num - target)//x
        
        return ans

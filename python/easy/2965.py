class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        hash_map = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                hash_map[grid[i][j]] += 1
        
        ans = [0] * 2
        for i in range(1, len(grid) * len(grid) + 1):
            if hash_map[i] > 1:
                ans[0] = i
            elif not hash_map[i]:
                ans[1] = i
        return ans
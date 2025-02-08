class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        curr_cons = 0
        for num in nums:
            if num == 1:
                curr_cons += 1
            else:
                max_cons = max(max_cons, curr_cons)
                curr_cons = 0

        max_cons = max(max_cons, curr_cons)
        
        return max_cons
            
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # 1st solution
        # parity = True
        # if nums[0] % 2 == 1:
        #     parity = False
        
        # for i in range(1, len(nums)):
        #     parity = not parity
        #     if parity == True and nums[i] % 2 == 1:
        #         return False
            
        #     if parity == False and nums[i] % 2 == 0:
        #         return False

        # return True

        # 2nd solution
        
        for i in range(1, len(nums)):
            if nums[i-1] % 2 == nums[i] % 2:
                return False
        return True

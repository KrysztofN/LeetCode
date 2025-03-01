class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr = []
        zero_count = 0
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                arr.append(nums[i] * 2)
                nums[i+1] = 0
            else:
                if nums[i] == 0:
                    zero_count += 1
                else:
                    arr.append(nums[i])

        arr.append(nums[-1])

        for _ in range(zero_count):
            arr.append(0)
        
        return arr
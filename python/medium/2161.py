class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # smaller_than_pivot = []
        # greater_than_pivot = []
        # equal_to_pivot = []
        # ans = []

        # for num in nums:
        #     if num < pivot:
        #         smaller_than_pivot.append(num)
        #     if num > pivot:
        #         greater_than_pivot.append(num)
        #     if num == pivot:
        #         equal_to_pivot.append(num)
        
        # ans = smaller_than_pivot + equal_to_pivot + greater_than_pivot
        # return ans

        # O(1) space
        left, right = 0, len(nums) - 1
        a = nums.index(pivot)
        nums.append(nums.pop(a))

        while left <= right:
            if nums[left] <= pivot:
                left += 1
            elif nums[left] > pivot:
                nums.append(nums[left])
                nums.pop(left)
                right -= 1

        left = 0
        while left < right:
            if nums[left] == pivot:
                nums[left], nums[left+1] = nums[left + 1], nums[left]
            left += 1
        return nums

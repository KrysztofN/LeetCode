class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        def bin_search(left_bound):
            left, right = 0 , len(nums) - 1
            target = 0
            while left <= right:
                mid = left + (right - left)//2

                if nums[mid] < target:
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1
                
                elif nums[mid] == target:
                    if left_bound:
                        right = mid - 1
                    else:
                        left = mid + 1
            return left
        
        neg = len(nums[:bin_search(1)])
        pos = len(nums[bin_search(0):])
        return max(pos, neg)

           
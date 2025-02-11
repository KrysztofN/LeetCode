class Solution:
    def check(self, nums: List[int]) -> bool:
        # 1st approach
        # n = len(nums)
        # for i in range(n):
        #     set_flag = 0
        #     last_seen = nums[i]
        #     for j in range(i+1, n+i):
        #         k = j % n
        #         if nums[k] < last_seen:
        #             set_flag = 1
        #             break
        #         last_seen = nums[k]
        #     if not set_flag:
        #         return True
        # return False

        # Optimized

        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False
        
        return True
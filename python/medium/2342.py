class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        sum_list = defaultdict(list)
        for i in range(len(nums)):
            # processing digit sum
            curr = nums[i]
            digit_sum = 0
            while curr:
                digit_sum += curr % 10
                curr = curr // 10
            heapq.heappush(sum_list[digit_sum], -nums[i])
        # for num in nums:
        #     # processing digit sum
        #     digit_sum = sum(int(x) for x in str(num))
        #     heapq.heappush(sum_list[digit_sum], -num)
        
        max_sum = -1

        for values in sum_list.values():
            if len(values) > 1:
                first = -heapq.heappop(values)
                second = -heapq.heappop(values)
                max_sum = max(max_sum, first + second)

        return max_sum



        




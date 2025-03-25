class Solution:
    def addDigits(self, num: int) -> int:

        # Naive approach
        # def int_sum(num):
        #     int_summ = 0
        #     for n in str(num):
        #         int_summ += int(n)
        #     return int_summ

        # while int_sum(num) > 9:
        #     num = int_sum(num)

        # return int_sum(num)

        # Optimal approach
        if num < 10:
            return num
        
        if num % 9 == 0:
            return 9

        return (num % 9)
        
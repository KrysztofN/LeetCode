class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partition(i, curr: int, target:int, string:str):
            if i == len(string) and curr == target:
                return True
            
            for j in range(i, len(string)):
                if partition(j + 1, curr + int(string[i:j+1]), target, string):
                    return True
            return False

        punishment = 0

        for i in range(1, n + 1):
            if partition(0, 0, i,str(i*i)):
                punishment += i*i
        return punishment
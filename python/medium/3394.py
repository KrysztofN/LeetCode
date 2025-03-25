class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        horizontal_arr = [[rec[0], rec[2]] for rec in rectangles] 
        vertical_arr = [[rec[1], rec[3]] for rec in rectangles] 

        horizontal_arr.sort()
        vertical_arr.sort()

        return True if max(self.non_overlap_count(horizontal_arr), self.non_overlap_count(vertical_arr)) >= 3 else False

    
    def non_overlap_count(self, coordinates):
        count = 0
        prev_end = -1
        for start, end in coordinates:
            if prev_end <= start:
                count += 1
            prev_end = max(prev_end, end)
        return count

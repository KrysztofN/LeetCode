class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_matrix = [i for s in matrix for i in s]
        
        i,j = 0, len(flattened_matrix) - 1
        mid = 0
        while i <= j:
            mid = i + (j - i) // 2
            if target > flattened_matrix[mid]:
                i = mid + 1
            elif target < flattened_matrix[mid]:
                j = mid - 1
            elif target == flattened_matrix[mid]:
                return True

        return False
        

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] < arr[0]:
            return False
        
        direction = 0 
        for i in range(1, len(arr)):
            if direction > 1:
                return False
            
            if arr[i] == arr[i-1]:
                return False
            
            if arr[i] > arr[i-1] and direction % 2 == 1:
                direction += 1
            
            elif arr[i] < arr[i-1] and direction % 2 == 0:
                direction += 1

        return True if direction == 1 else False

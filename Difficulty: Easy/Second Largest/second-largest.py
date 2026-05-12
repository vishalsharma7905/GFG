class Solution:
    def getSecondLargest(self, arr):
        
        largest = -1
        second_largest = -1
        
        for num in arr:
            
            # New largest found
            if num > largest:
                second_largest = largest
                largest = num
            
            # Update second largest
            elif num > second_largest and num != largest:
                second_largest = num
        
        return second_largest
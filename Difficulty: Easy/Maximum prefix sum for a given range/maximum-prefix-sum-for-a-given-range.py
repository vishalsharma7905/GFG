class Solution:
    def maxPrefixes(self, arr, leftIndex, rightIndex):
        result = []
        
        # Loop through each query
        for l, r in zip(leftIndex, rightIndex):
            curr_sum = 0
            max_sum = float('-inf')
            
            # Calculate prefix sums in the range
            for i in range(l, r + 1):
                curr_sum += arr[i]
                max_sum = max(max_sum, curr_sum)
            
            result.append(max_sum)
        
        return result
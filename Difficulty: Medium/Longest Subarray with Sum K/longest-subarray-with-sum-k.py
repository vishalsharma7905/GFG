class Solution:
    def longestSubarray(self, arr, k):
        
        prefix_sum = 0
        max_len = 0
        
        # Dictionary to store first occurrence of prefix sum
        prefix_map = {}
        
        for i in range(len(arr)):
            
            prefix_sum += arr[i]
            
            # If total sum itself becomes k
            if prefix_sum == k:
                max_len = i + 1
            
            # Check if (prefix_sum - k) exists
            if (prefix_sum - k) in prefix_map:
                length = i - prefix_map[prefix_sum - k]
                max_len = max(max_len, length)
            
            # Store first occurrence only
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return max_len
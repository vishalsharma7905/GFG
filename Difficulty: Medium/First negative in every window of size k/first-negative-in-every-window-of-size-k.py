from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        
        q = deque()
        ans = []
        
        # Process first window
        for i in range(k):
            if arr[i] < 0:
                q.append(arr[i])
        
        # Store answer for first window
        if q:
            ans.append(q[0])
        else:
            ans.append(0)
        
        # Slide the window
        for i in range(k, len(arr)):
            
            # Remove element going out of window
            if q and arr[i-k] == q[0]:
                q.popleft()
            
            # Add new negative element
            if arr[i] < 0:
                q.append(arr[i])
            
            # Store answer
            if q:
                ans.append(q[0])
            else:
                ans.append(0)
        
        return ans
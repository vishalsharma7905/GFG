class Solution:
    def leaders(self, arr):
        leaders = []
        
        max_right = arr[-1]
        leaders.append(max_right)
        
        # Traverse from right to left
        for i in range(len(arr)-2, -1, -1):
            if arr[i] >= max_right:
                max_right = arr[i]
                leaders.append(arr[i])
        
        # Reverse because we collected from right side
        leaders.reverse()
        
        return leaders
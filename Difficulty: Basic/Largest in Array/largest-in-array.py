class Solution:
    def largest(self, arr):
        n = len(arr)
        largest = arr[0]
        for i in range(0,n):
          largest = max(largest, arr[i])
        return largest
            
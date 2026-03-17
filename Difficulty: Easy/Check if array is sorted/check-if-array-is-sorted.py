class Solution:
    def isSorted(self, arr) -> bool:
        n = len(arr)
        for i in range(n-1):
          if arr[i]>arr[i+1]:
              return False
        return True
       
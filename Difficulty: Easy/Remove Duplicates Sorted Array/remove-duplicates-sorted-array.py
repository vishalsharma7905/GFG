class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        seen = set()
        result = []
        for i in range (0,n):
            if arr[i] not in seen:
                seen.add(arr[i])
                result.append(arr[i])
        return result
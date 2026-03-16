class Solution:
    def largest(self, arr):
        largest = arr[0]

        for i in arr:
            if i > largest:
                largest = i

        return largest
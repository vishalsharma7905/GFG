class Solution:
    def getSecondLargest(self, arr):
        largest = second = -1
        for i in arr:
            if i > largest:
                second = largest
                largest = i
            elif i > second and i != largest:
                second = i
        return second
        
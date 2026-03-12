class Solution:
    
    def merge(self, arr, l, m, r):
        L = arr[l:m+1]
        R = arr[m+1:r+1]

        i = j = 0
        k = l

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)
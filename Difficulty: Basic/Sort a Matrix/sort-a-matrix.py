class Solution:
    def sortedMatrix(self, mat):

        # Convert matrix into single list
        arr = []

        for row in mat:
            for num in row:
                arr.append(num)

        # Sort the list
        arr.sort()

        n = len(mat)
        k = 0

        # Put sorted elements back into matrix
        for i in range(n):
            for j in range(n):
                mat[i][j] = arr[k]
                k += 1

        return mat
class Solution:
    def boundaryTraversal(self, mat):

        result = []

        rows = len(mat)
        cols = len(mat[0])

        # Top row
        for j in range(cols):
            result.append(mat[0][j])

        # Right column
        for i in range(1, rows):
            result.append(mat[i][cols - 1])

        # Bottom row
        if rows > 1:
            for j in range(cols - 2, -1, -1):
                result.append(mat[rows - 1][j])

        # Left column
        if cols > 1:
            for i in range(rows - 2, 0, -1):
                result.append(mat[i][0])

        return result
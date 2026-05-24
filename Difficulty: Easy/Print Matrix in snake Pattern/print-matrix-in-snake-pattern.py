class Solution:
    def snakePattern(self, matrix):
        result = []

        for i in range(len(matrix)):

            # Even row -> left to right
            if i % 2 == 0:
                for j in range(len(matrix[i])):
                    result.append(matrix[i][j])

            # Odd row -> right to left
            else:
                for j in range(len(matrix[i]) - 1, -1, -1):
                    result.append(matrix[i][j])

        return result
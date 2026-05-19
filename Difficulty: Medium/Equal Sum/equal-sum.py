class Solution:
    def equilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for num in arr:
            total_sum -= num   # right sum

            if left_sum == total_sum:
                return "true"

            left_sum += num

        return "false"
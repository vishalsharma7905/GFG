class Solution:
    def sortedCount(self, N, M, Mat):
        count = 0
        
        for row in Mat:
            inc = True
            dec = True
            
            for i in range(M - 1):
                if row[i] >= row[i + 1]:
                    inc = False
                if row[i] <= row[i + 1]:
                    dec = False
            
            if inc or dec:
                count += 1
        
        return count
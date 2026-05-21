from collections import Counter

class Solution:
    
    def search(self, pat, txt):
        
        k = len(pat)
        
        # Frequency map of pattern
        pat_count = Counter(pat)
        
        # Frequency map of current window
        window_count = Counter()
        
        ans = 0
        
        for i in range(len(txt)):
            
            # Add current character
            window_count[txt[i]] += 1
            
            # Remove character out of window
            if i >= k:
                if window_count[txt[i-k]] == 1:
                    del window_count[txt[i-k]]
                else:
                    window_count[txt[i-k]] -= 1
            
            # Compare maps
            if window_count == pat_count:
                ans += 1
        
        return ans
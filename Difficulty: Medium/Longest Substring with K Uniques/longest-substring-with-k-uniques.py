class Solution:
    def longestKSubstr(self, s, k):
        
        left = 0
        max_len = -1
        
        freq = {}
        
        for right in range(len(s)):
            
            # Add current character
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1
            
            # Shrink window if unique chars > k
            while len(freq) > k:
                
                freq[s[left]] -= 1
                
                if freq[s[left]] == 0:
                    del freq[s[left]]
                
                left += 1
            
            # Check if exactly k unique chars
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)
        
        return max_len
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force solution
        best = 1
        res = (0,1)
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1] and best < j-i:
                    best = j-i
                    res = (i,j)
        
        return s[res[0]:res[1]]

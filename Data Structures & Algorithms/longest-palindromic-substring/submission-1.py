class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force solution
        n = len(s)
        best = 1
        res = (0,1)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if best < j-i+1:
                            res = (i,j+1)
                            best = j-i+1
                    
        return s[res[0]:res[1]]

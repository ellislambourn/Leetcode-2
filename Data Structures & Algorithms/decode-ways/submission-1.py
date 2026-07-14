class Solution:
    def numDecodings(self, s: str) -> int:
        # recursive solution.
        # only recurses if there is a 1 or 2 and something after.
        n = len(s)
        dp = {n : 1}

        def rec(i):
            if i in dp:
                return dp[i]

            if i == n:
                return 1

            if s[i] == "0":
                return 0

            res = rec(i +1) # take 1 digit

            if s[i] == "1" and i+1 < n:
                res += rec(i + 2)
            if s[i] == "2" and i+1 < n and s[i+1] in "0123456":
                res +=  rec(i + 2)
            dp[i] = res
            
            return res
        
        return rec(0)



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if word not in s:
                wordDict.remove(word)
        # the recursuve solution will TLE.
        # can create a cache that says dp[i] is able to reach the end. 
        dp = [None] * (len(s) + 1)
        dp[len(s)] = True

        def dfs(i):
            if dp[i]:
                return True
            if dp[i] == False:
                return False
            if i == len(s):
                return True
            
            possible = wordDict.copy()
            for word in possible:
                if s[i:i+len(word)] == word:
                    if dfs(i+len(word)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
                
        return dfs(0)
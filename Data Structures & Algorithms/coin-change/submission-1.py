class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # alter the recursive version with memoisation.

        dp = [[float("inf")] * (len(coins)+1) for _ in range(amount+1)]
        dp[0][0] = 0
        # dp[amount][i]

        coins.sort()
        
        def dfs(amount, i):
            if dp[amount][i] != float("inf"):
                return dp[amount][i]

            if amount == 0:
                return 0
            if i == len(coins) or amount < coins[i]:
                return float("inf")
            
           
            res = min(
                dfs(amount, i+1), # not choosing this coin
                1 + dfs(amount - coins[i], i) # choosing the coin
            )

            dp[amount][i] = res
            return res

        res = dfs(amount, 0)
        res = res if res != float("inf") else -1
        return res
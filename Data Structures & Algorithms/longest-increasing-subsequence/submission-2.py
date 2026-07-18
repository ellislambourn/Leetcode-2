class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recursive with dp
        dp = [{} for _ in range(len(nums))]

        #returns the LIS length starting from index i. 
        def dfs(currMax,i) -> int:
            if i >= len(nums):
                return 0
            if currMax in dp[i]:
                return dp[i][currMax]
            
            if nums[i] <= currMax:
                out = dfs(currMax, i+1)
            else:            
                out1 = dfs(currMax, i+1) # dont choose this
                out2 = 1 + dfs(nums[i], i+1) # choose this
                out = max(out1, out2)
            
            dp[i][currMax] = out        
            return out
            


        res = dfs(-1001, 0)
        return res
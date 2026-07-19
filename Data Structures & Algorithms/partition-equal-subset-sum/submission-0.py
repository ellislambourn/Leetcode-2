class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if self.isOdd(total):
            return False

        half = total // 2

        # dp[(i, remaining)] stores the result of dfs(i, remaining)
        dp = {}

        def dfs(i: int, remaining: int) -> bool:
            if remaining == 0:
                return True

            if i >= len(nums) or remaining < 0:
                return False

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            skip = dfs(i + 1, remaining)
            include = dfs(i + 1, remaining - nums[i])

            dp[(i, remaining)] = skip or include
            return dp[(i, remaining)]

        return dfs(0, half)

    def isOdd(self, num: int) -> bool:
        return num % 2 != 0
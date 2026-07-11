class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses: List[int]) -> int:
            rob1 = 0
            rob2 = 0

            for money in houses:
                rob1, rob2 = rob2, max(rob2, rob1 + money)

            return rob2

        return max(
            rob_line(nums[:-1]), 
            rob_line(nums[1:])    
        )
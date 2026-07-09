class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            bestCost = min(cost[i-1], cost[i-2])
            cost[i] += bestCost
        return min(cost[-1], cost[-2])
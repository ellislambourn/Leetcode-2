class Solution:
    def climbStairs(self, n: int) -> int:
        # dp top down

        array = [0]* (n+1)
        array[-1], array[-2] = 1, 1
        for i in reversed(range(len(array)-2)):
            array[i] = array[i+1] + array[i+2]

        return array[0]
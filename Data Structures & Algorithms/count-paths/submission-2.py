from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # could use dp and work backwards from the finish or I just spot this is pascals triangle.

        n = n +m -2
        r = m -1

        return pascal(n,r)

def pascal(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

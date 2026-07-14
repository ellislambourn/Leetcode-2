class Solution:
    def countSubstrings(self, s: str) -> int:
        # centre - out approach
        n = len(s)
        res = n
        for i in range(n):
            # do odd palindrome check for s[i]
            res += self.oddPCount(s,i)
            # do even p check for s[i]
            res += self.evenPCount(s,i)
        return res
    def oddPCount(self, s, i) -> int:
        n = len(s)
        l = i - 1
        r = i + 1
        count = 0

        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

    def evenPCount(self, s, i) -> int:
        l = i
        r = i + 1
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
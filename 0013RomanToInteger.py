class Solution:
    def romanToInt(self, s: str) -> int:
        curr, prev, a = 0, 0, 0
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range (len(s)-1, -1, -1):
            curr = romans[s[i]]
            if curr < prev:
                a = a - curr
            else:
                a = a + curr
            prev = curr
        return a    
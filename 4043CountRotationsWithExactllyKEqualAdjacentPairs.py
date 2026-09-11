class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        E = 0
        for i in range(n):
            if s[i] == s[(i+1) % n]:
                E += 1
        if k == E:
            return n - E
        elif k == E - 1:
            return E
        else:
            return 0
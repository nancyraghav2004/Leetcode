class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n)
        if n[0] == str(x):
            return False
            
        for i in n:
            if i == str(x):
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    p = 101
    q = 0
    print(s.validDigit(p,q))
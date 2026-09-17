class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    x = 121
    print(s.isPalindrome(x))
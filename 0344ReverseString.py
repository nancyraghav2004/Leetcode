from typing import List

# My Solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left = left+1
            right = right - 1

# Good Solution
class Solution:
    def reverseString(self, s):
        s[:] = s[::-1]

if __name__ == "__main__":
    solution = Solution()
    s = ["h","e","l","l","o"]
    print(solution.reverseString(s))
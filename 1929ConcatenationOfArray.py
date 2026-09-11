from typing import List

# My Solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        return nums

# Good Solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

if __name__ == "__main__":
    sol = Solution()
    num = [1, 2, 3]
    print(sol.getConcatenation(num))
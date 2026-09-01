# My Solution to LeetCode problem 136: Single Number
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] not in nums[:i] + nums[i+1:]:
                a = nums[i]
        return a

if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 2, 1, 2]
    result = solution.singleNumber(nums)
    print(result)  # Output: 4



# Standard Solution using XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 2, 1, 2]
    result = solution.singleNumber(nums)
    print(result)  # Output: 4
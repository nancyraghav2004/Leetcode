from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] in nums[:i] + nums[i+1:]:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    result = solution.majorityElement(nums)
    print(result)  # Output: True


# Solution where all testcase passed
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    result = solution.containsDuplicate(nums)
    print(result)  # Output: True
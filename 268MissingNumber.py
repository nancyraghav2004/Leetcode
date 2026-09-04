from typing import List

# Bad code
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)):
            if nums[0] != 0:
                return 0
            if nums[i] + 1 not in nums:
                return (nums[i]+1)

if __name__ == "__main__":
    s = Solution()
    arr = [3, 0, 1]
    print(s.missingNumber(arr))



# Good Approach
class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum
if __name__ == "__main__":
    s = Solution()
    arr = [3, 0, 1]
    print(s.missingNumber(arr))
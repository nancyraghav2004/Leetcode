class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()

        a = 1

        for num in nums:
            if num == a:
                a += 1
            elif num > a:
                return a

        return a

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

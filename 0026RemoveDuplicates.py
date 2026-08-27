from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 4]
    k = solution.removeDuplicates(nums)
    print(k)  # Output: 5
    print(nums[:k])  # Output: [0, 1, 2, 3, 4]
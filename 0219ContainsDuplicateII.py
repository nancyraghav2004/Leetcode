from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    result = solution.containsNearbyDuplicate(nums, k)
    print(result)  # Output: True
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return max(count, key=count.get)

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    result = solution.majorityElement(nums)
    print(result)  # Output: 3

# Standard Solution using Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    result = solution.majorityElement(nums)
    print(result)  # Output: 3


# Another Standard Solution using 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    result = solution.majorityElement(nums)
    print(result)  # Output: 3
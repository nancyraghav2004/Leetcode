from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum = left_sum + nums[i]
        return -1 

if __name__ == "__main__":
    s = Solution()
    num = [1, 7, 3, 6, 5, 6]
    print(s.pivotIndex(num))

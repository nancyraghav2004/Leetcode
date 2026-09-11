from typing import List

# My Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                left = left + 1


# Good Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            summation = numbers[i] + numbers[j]
            if summation == target:
                return [i+1, j+1]
            elif summation > target:
                j -= 1
            else:
                i += 1

from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        a = 0
        for values in count.values():
            b = values * (values-1)//2
            a = a + b
        return (a)

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    print(s.numIdenticalPairs(nums))
    
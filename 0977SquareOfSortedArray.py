from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []
        for num in nums:
            p = abs(num * num)
            a.append(p)
        a.sort()
        return a
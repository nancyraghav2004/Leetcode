from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set()
        for num in nums:
            if num in a:
                return num
            else:
                a.add(num)
from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = []
        for row in accounts:
            total = 0

            for nums in row:
                total = total + nums
            a.append(total)
        return max(a)

    
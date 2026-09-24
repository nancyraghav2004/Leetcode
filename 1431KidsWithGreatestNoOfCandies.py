from typing import List

#My Solution
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        output = []
        greatest = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                output.append(True)
            else:
                output.append(False)
        return (output)


# Good Solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        return [True if candy + extraCandies >= max_candies else False for candy in candies]
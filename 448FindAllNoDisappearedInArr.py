from typing import List
from collections import Counter

# Good Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        counts=[0]*(n+1)
        for num in nums:
            counts[num]=1
        return [i for i in range(1,n+1) if counts[i]<1]


#My Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = []
        n = Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in n:
                a.append(i)
        return a

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 4, 1, 23, 12, 31, 23, 213, 2, 14, 214, 1]
    print(s.findDisappearedNumbers(nums))
from typing import List

# My Solution
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = list(set(nums1))
        set2 = list(set(nums2))
        ans = []
        for num in set1:
            if num in set2:
                set1.remove(num)
                set.remove(num)
        ans.append(set1)
        ans.append(set2)
        return ans

# Good Solution
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        return [list(a-b),list(b-a)]

if __name__ == "__main__":
    s = Solution()
    num1 = [1,2, 3]
    num2 = [2, 4, 5]
    print(s.findDifference(num1, num2))
    
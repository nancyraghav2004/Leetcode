from typing import List
from collections import Counter

# My Solution
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         output = []
#         for num in nums1:
#             if num in nums2:
#                 output.append(num)
#                 nums2.remove(num)
#         return output

# Good Solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_c = Counter(nums1)
        n2_c = Counter(nums2)

        result = []
        for key in n1_c:
            if key in n2_c:
                result.extend([key] * min(n1_c[key], n2_c[key]))
        return result

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2]
    print(s.intersect(nums1, nums2))
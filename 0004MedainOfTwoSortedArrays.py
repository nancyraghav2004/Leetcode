from typing import List

# My Solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        n = len(num)
        if n%2 != 0:
            return (num[(n//2)])
        else:
            return ((num[n//2] + num[n//2 - 1])/2)

# Good Solution
class Solution:

  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    half_len = (m + n + 1) // 2

    while left <= right:
      i = (left + right) // 2
      j = half_len - i

      max_left1 = float("-inf") if i == 0 else nums1[i - 1]
      min_right1 = float("inf") if i == m else nums1[i]

      max_left2 = float("-inf") if j == 0 else nums2[j - 1]
      min_right2 = float("inf") if j == n else nums2[j]

      if max_left1 <= min_right2 and max_left2 <= min_right1:
        if (m + n) % 2 == 1:
          return float(max(max_left1, max_left2))
        return (
            max(max_left1, max_left2) + min(min_right1, min_right2)
        ) / 2.0
      elif max_left1 > min_right2:
        right = i - 1
      else:
        left = i + 1

    return 0.0

if __name__ == '__main__':
   s = Solution()
   num1 = [1, 2]
   num2 = [3, 4]
   print(s.findMedianSortedArrays(num1, num2))

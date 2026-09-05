from typing import List

# Good Solution
class Solution():
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        s1, s2 = set(nums1), set(nums2)

        result = []

        for num in s1:
            if num in s2:
                result.append(num)

        return result


# My Solution
class Solution():
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = ()
        for num in nums1:
            if num in nums2:
                output.add(num)
        return list(output)

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersection(nums1, nums2))
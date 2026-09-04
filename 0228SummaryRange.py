from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        start = 0
        end = 0
        i = 0
        while i <= len(nums)-1:
            start = nums[i]
            end = nums[i]
            while i < len(nums) - 1 and nums[i+1] == nums[i]+1:
                i = i+1
                end = nums[i]
            i = i+1
            if start != end:
                output.append(str(start) + '->' + str(end))
            else:
                output.append(str(end))
        return (output)

if __name__ == '__main__':
    solution = Solution()
    arr = [0, 1, 2, 4, 5, 7]
    print(solution.summaryRanges(arr))

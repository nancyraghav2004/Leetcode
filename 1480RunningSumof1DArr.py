class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = nums[0]
        output = []
        output.append(a)
        for i in range(1, len(nums)):
            output.append(output[i-1] + nums[i])
        return (output)
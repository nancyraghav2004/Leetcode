class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = num
        nums = list(str(num))
        for i in range(len(nums)):
            if nums[i] == '9':
                nums[i] = '6'

            elif nums[i] == '6':
                nums[i] = '9'

            max_num = max(max_num, int(''.join(nums)))
            nums = list(str(num))
        return max_num

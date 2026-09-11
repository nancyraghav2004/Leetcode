class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = 1, 1
        n = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = n
            n = n * nums[i]
        for j in range(len(nums)-1, -1, -1):
            output[j] = output[j] * suf
            suf = suf * nums[j]
        return output
                
if __name__ == "__main__":
    s = Solution()
    num = [1, 2, 3, 4]
    print(s.productExceptSelf(num))
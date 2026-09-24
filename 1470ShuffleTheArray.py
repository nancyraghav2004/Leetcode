from typing import List

# My Solution
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p = nums[0]
        output=[]
        output.append(p)
        for i in range(n):
            a = nums[i+n]
            output.append(a)
            output.append(nums[i+1])
        return (output[:len(nums)])

# Good Solution
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0] * (2*n)
        even = 0 
        odd = n
        for i in range(0,2*n): 
            if i % 2 == 0 :
                arr[i] = nums[even] 
                even += 1
            else: 
                arr[i] = nums[odd]
                odd += 1 
        return arr
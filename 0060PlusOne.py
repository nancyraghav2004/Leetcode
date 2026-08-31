from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        result = result + 1
        return (list(map(int, str(result))))

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))


# Second Solution
# arr = [1, 2, 3]
# n = 0
# for i in arr:
#     n = n*10 + i
# print(n)
# n = n+1
# r = []
# while n > 0:
#     r.append(n%10)
#     n = n//10
# print(r[::-1])
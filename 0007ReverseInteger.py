#My Solution
class Solution:
    def reverse(self, x: int) -> int:
        total  = 0
        temp = abs(x)
        while temp > 0:
            digit = temp % 10
            total = total * 10 + digit
            temp = temp // 10
        if x < 0:
            total = -total
        if total < -2147483648 or total > 2147483648:
            return 0
        return total

# Good Solution
class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        reversed_num *= sign
        # 32-bit signed integer range
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num

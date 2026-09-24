#Brute Force 
# s = babad
class Solution:
    def longestPalindrome(self, s: str) -> str:

        answer = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):

                sub = s[i:j]

                if sub == sub[::-1]:
                    if len(sub) > len(answer):
                        answer = sub

        return answer

#Brute Force + 2 Pointer
class Solution:
    def longestPalindrome(self, s: str) -> str:

        answer = ""

        for i in range(len(s)):
            for j in range(i, len(s)):

                left = i
                right = j
                is_palindrome = True

                while left < right:

                    if s[left] != s[right]:
                        is_palindrome = False
                        break

                    left += 1
                    right -= 1

                if is_palindrome and (j - i + 1) > len(answer):
                    answer = s[i:j + 1]

        return answer

#Expand Aroung Centre
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        answer = ""

        def expand(left, right):

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return s[left + 1:right]

        for i in range(len(s)):

            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(answer):
                answer = odd

            if len(even) > len(answer):
                answer = even

        return answer

#Dynamic Programming
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]

        answer = s[0]

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check substrings of length 2 or more
        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:

                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if length > len(answer):
                            answer = s[i:j + 1]

        return answer

#Manacher's Algorithm
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        p = [0] * n

        center = 0
        right = 0

        for i in range(1, n - 1):

            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        max_len = max(p)
        center_index = p.index(max_len)

        start = (center_index - max_len) // 2

        return s[start:start + max_len]



    #             Longest Palindromic Substring
    #                        │
    #       ┌────────────────┼────────────────┐
    #       ↓                ↓                ↓
    #  Brute Force      Expand Center         DP
    #    O(n³)             O(n²)             O(n²)
    #       │                │                 │
    #   easiest          LEARN THIS          later
                                           
    #                        ↓
    #                    Manacher's
    #                        O(n)

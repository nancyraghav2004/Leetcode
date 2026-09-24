from typing import List 

# My Solution
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        output = []
        for i in range(len(indices)):
            a = indices.index(i)
            output.append(s[a])
        return (''.join(output))

# Good Solution
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [""] * len(s)

        for i in range(len(s)):
            arr[indices[i]] = s[i]

        return "".join(i for i in arr)
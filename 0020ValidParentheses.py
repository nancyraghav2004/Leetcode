from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        a = {"(": ")", "[": "]", "{": "}"}
        b = []
        for i in s:
            if i in a:
                b.append(i)
            elif i in a.values():
                if not b:
                    return False
                if a[b[-1]] == i:
                    b.pop()
                else:
                    return False
        return not b

if __name__ == "__main__":
    s = Solution()
    o = "{({})}[]"
    print(s.isValid(o))
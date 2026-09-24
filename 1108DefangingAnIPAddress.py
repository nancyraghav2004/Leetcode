# My Solution
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace(".", "[.]")
        return address

# Good Solution Acc to leetcode
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

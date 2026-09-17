class Solution:
    def bitwiseComplement(self, n: int) -> int:
        complement = ''
        binary = bin(n)[2:]
        for digit in binary:
            if digit == '0':
                complement += '1'
            else:
                complement += '0'
        comp = int(complement, 2)
        return comp
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        plus = 0
        minus = 0
        for op in operations:
            if op == "--X" or op == "X--":
                minus += 1
            else:
                plus += 1
        return plus-minus
        
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        triangle = [[1]]  # Initialize the triangle with the first row
        for i in range(1, numRows):
            row = [1]  # Start each row with a 1
            for j in range(1, i):
                # Each element is the sum of the two elements above it
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # End each row with a 1
            triangle.append(row)
        return triangle

if __name__ == "__main__":
    solution = Solution()
    numRows = 5
    result = solution.generate(numRows)
    for row in result:
        print(row)  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
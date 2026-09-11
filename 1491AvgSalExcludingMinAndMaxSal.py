from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
       max_sal = max(salary)
       salary.remove(max_sal)
       min_sal = min(salary)
       salary.remove(min_sal)
       avg_sal = sum(salary)/len(salary)
       return avg_sal

if __name__ == '__main__':
    s = Solution()
    sal = [1000, 2000, 3000, 8000]
    print(s.average(sal))
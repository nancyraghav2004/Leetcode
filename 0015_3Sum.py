class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        a = []
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    a.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    right = right - 1
                else:
                    left = left + 1
        return a

# Good Solution
from collections import Counter
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n < 3:
            return []

        # Counter construction costs more than a direct check.
        if n == 3:
            return [nums] if nums[0] + nums[1] + nums[2] == 0 else []

        # For small inputs, the simpler O(n²) algorithm wins
        # because it has very little setup overhead.
        if n < 20:
            nums.sort()
            result = []

            for i in range(n - 2):
                first = nums[i]

                if first > 0:
                    break

                if i and first == nums[i - 1]:
                    continue

                left = i + 1
                right = n - 1

                while left < right:
                    total = first + nums[left] + nums[right]

                    if total < 0:
                        left += 1

                    elif total > 0:
                        right -= 1

                    else:
                        result.append([
                            first,
                            nums[left],
                            nums[right]
                        ])

                        left_value = nums[left]
                        right_value = nums[right]

                        left += 1
                        right -= 1

                        while (
                            left < right
                            and nums[left] == left_value
                        ):
                            left += 1

                        while (
                            left < right
                            and nums[right] == right_value
                        ):
                            right -= 1

            return result

        counts = Counter(nums)
        zero_count = counts.pop(0, 0)

        result = []
        append = result.append

        if zero_count >= 3:
            append([0, 0, 0])

        if not counts:
            return result

        unique = sorted(counts)
        counts_set = set(unique)

        # Handle answers containing zero or a repeated number.
        for num in unique:
            if (
                num < 0
                and zero_count
                and -num in counts_set
            ):
                append([num, 0, -num])

            if not num & 1:
                candidate = -(num >> 1)

                if (
                    candidate in counts_set
                    and counts[candidate] >= 2
                ):
                    if num < candidate:
                        append([num, candidate, candidate])
                    else:
                        append([candidate, candidate, num])

        if len(unique) < 2:
            return result

        first_unique = unique[0]
        last_unique = unique[-1]

        a = -last_unique // 2
        start = bisect_right(
            unique,
            a if a > first_unique else first_unique
        )

        a = -(first_unique // 2)
        stop = bisect_left(
            unique,
            a if a < last_unique else last_unique
        )

        # Batch construction pays off only when there are enough
        # unique values spread sparsely across a large range.
        use_batching = (
            len(unique) > 100
            and last_unique - first_unique + 1 > len(unique) * 4
        )

        if use_batching:
            for i in range(start, stop):
                middle = unique[i]

                right_start = (
                    bisect_right(unique, middle * -2)
                    if middle < 0
                    else i + 1
                )

                right_stop = bisect_right(
                    unique,
                    -first_unique - middle
                )

                target = -middle

                result.extend([
                    [target - right, middle, right]
                    for right in unique[right_start:right_stop]
                    if target - right in counts_set
                ])

        else:
            for i in range(start, stop):
                middle = unique[i]

                right_start = (
                    bisect_right(unique, middle * -2)
                    if middle < 0
                    else i + 1
                )

                right_stop = bisect_right(
                    unique,
                    -first_unique - middle
                )

                for right in unique[right_start:right_stop]:
                    left = -middle - right

                    if left in counts_set:
                        append([left, middle, right])

        return result


#My Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            # Remove characters until there is no duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character
            seen.add(s[right])

            # Update maximum
            max_len = max(max_len, len(seen))

        return max_len

# Good Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_ptr = 0
        existing_string = set()
        global_max = 0
        for r_ptr in range(len(s)):
            while s[r_ptr] in existing_string:
                existing_string.remove(s[l_ptr])
                l_ptr += 1
            existing_string.add(s[r_ptr])
            global_max = max(global_max, len(existing_string))
        return global_max
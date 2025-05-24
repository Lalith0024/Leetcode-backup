class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        longest = 0
        a = 0  # Left pointer of the sliding window

        for b, char in enumerate(s):
            if char in last_seen and last_seen[char] >= a:
                # Move the left pointer to avoid duplicate
                a = last_seen[char] + 1
            last_seen[char] = b  # Update the last seen index
            current_len = b - a + 1
            longest = max(longest, current_len)

        return longest

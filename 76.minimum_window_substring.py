"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""


class Solution:
    # O(s + t)
    def minWindow(self, s: str, t: str) -> str:
        words = {}
        for i in range(len(t)):
            words[t[i]] = words.get(t[i], 0) + 1
        start = 0
        length = 0
        best_start = -1
        best_length = len(s) + 1
        for end in range(len(s)):
            end_char = s[end]
            if end_char in words:
                words[end_char] -= 1
                if words[end_char] >= 0:
                    length += 1
            while (length == len(t)):
                start_char = s[start]
                if end - start + 1 < best_length:
                    best_length = end - start + 1
                    best_start = start
                if start_char in words:
                    words[start_char] += 1
                    if words[start_char] > 0:
                        length -= 1
                start += 1
        return "" if best_start == -1 else s[best_start:best_start + best_length]


print(Solution().minWindow("ABBCDA", "ABCD"))

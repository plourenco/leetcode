"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_start = max_end = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                start, end = self.expand(s, i - 1, i)
                if end - start > max_end - max_start:
                    max_start = start + 1
                    max_end = end
            if i > 1 and s[i] == s[i - 2]:
                start, end = self.expand(s, i - 2, i)
                if end - start > max_end - max_start:
                    max_start = start + 1
                    max_end = end
        return s[max_start:max_end] if max_start != max_end else s[max_start]

    def expand(self, s: str, start=0, end=0):
        while (start >= 0 and end < len(s) and s[start] == s[end]):
            end += 1
            start -= 1
        return start, end


print(Solution().longestPalindrome("aacabdkacaa"))  # aca
# print(Solution().longestPalindrome("defkabcdedcbajcccccc"))  # abcdedcba
# print(Solution().longestPalindrome("babad"))  # bab
# print(Solution().longestPalindrome("abb"))  # bb
# print(Solution().longestPalindrome("cbbd"))  # bb
# print(Solution().longestPalindrome("ccc"))  # ccc
# print(Solution().longestPalindrome("ccd"))  # cc
# print(Solution().longestPalindrome("caba"))  # aba
# print(Solution().longestPalindrome("bb"))  # bb
# print(Solution().longestPalindrome("aaaa"))  # aaaa

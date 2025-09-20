# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
#  A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (i.e., "ace" is a subsequence of
# "abcde" while "aec" is not).
#
#
#  Example 1:
#  Input: s = "abc", t = "ahbgdc"
# Output: true
#
#  Example 2:
#  Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
#  Constraints:
#
#
#  0 <= s.length <= 100
#  0 <= t.length <= 10⁴
#  s and t consist only of lowercase English letters.
#
#
#
# Follow up: Suppose there are lots of incoming
# s, say
# s1, s2, ..., sk where
# k >= 10⁹, and you want to check one by one to see if
# t has its subsequence. In this scenario, how would you change your code?
#
#  Related Topics Two Pointers String Dynamic Programming 👍 10496 👎 593


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # ----------------------------------------------------------
        # 1st idea: loop and slice
        # ----------------------------------------------------------
        #
        # for l in s:
        #     if l not in t:
        #         return False
        #
        #     cut_position = t.index(l) + 1
        #     t = t[cut_position:]
        #
        # return True

        # ----------------------------------------------------------
        # 2nd idea: 2-pointers solution
        # ----------------------------------------------------------
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


s = Solution()

assert s.isSubsequence("abc", "ahbgdc") == True
assert s.isSubsequence("axc", "ahbgdc") == False
assert s.isSubsequence("acb", "ahbgdc") == False
assert s.isSubsequence("aaaaaa", "bbaaaa") == False
# leetcode submit region end(Prohibit modification and deletion)

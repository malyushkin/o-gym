# For two strings s and t, we say "t divides s" if and only if s = t + t + t + .
# .. + t + t (i.e., t is concatenated with itself one or more times).
#
#  Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.
#
#
#  Example 1:
#
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
#
#  Example 2:
#
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
#
#  Example 3:
#
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
#
#  Constraints:
#
#
#  1 <= str1.length, str2.length <= 1000
#  str1 and str2 consist of English uppercase letters.
#
#
#  Related Topics Math String 👍 5807 👎 1614
from textwrap import shorten


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        from math import gcd

        if str1 + str2 == str2 + str1:
            # [Core] GCD – Greatest common divisor
            gcd_val = gcd(len(str1), len(str2))  # [Core] `math` lib
            shortest = min([str1, str2], key=(lambda x: len(x)))  # [Core] min with `key` attr

            return shortest[:gcd_val]

        else:
            # no such pattern
            return ""


s = Solution()
assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
assert s.gcdOfStrings("LEET", "CODE") == ""
assert s.gcdOfStrings("AAAAAA", "AAA") == "AAA"
assert s.gcdOfStrings("A", "AAAA") == "A"

# leetcode submit region end(Prohibit modification and deletion)

# Given an input string s, reverse the order of the words.
#
#  A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
#
#  Return a string of the words in reverse order concatenated by a single space.
#
#
#  Note that s may contain leading or trailing spaces or multiple spaces
# between two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
#
#
#  Example 1:
#
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
#
#  Example 2:
#
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
#
#
#  Example 3:
#
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁴
#  s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
#  There is at least one word in s.
#
#
#
#  Follow-up: If the string data type is mutable in your language, can you
# solve it in-place with O(1) extra space?
#
#  Related Topics Two Pointers String 👍 9876 👎 5457
from distutils.command.clean import clean


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # ----------------------------------------------------------
        # 1st idea: regex + manual reverse
        # ----------------------------------------------------------
        #
        # import re  # [Core] `re` lib
        #
        # s_cleaned = re.sub(r"\s{2,}", " ", s)  # [Core] regex
        # s_cleaned = s_cleaned.strip()  # [Core] strip() functions
        #
        # s_cleaned_list = s_cleaned.split(" ")
        # result_list = []
        #
        # while s_cleaned_list:
        #     result_list.append(s_cleaned_list.pop())
        #
        # return " ".join(result_list)
        #
        # Works fine, but uses regex and extra steps

        # ----------------------------------------------------------
        # 2nd idea: optimized / Pythonic approach
        # ----------------------------------------------------------
        #
        words = s.split()
        return " ".join(reversed(words))  # [Core] reversed


s = Solution()

assert s.reverseWords("the sky is blue") == "blue is sky the"
assert s.reverseWords("  hello world  ") == "world hello"
assert s.reverseWords("a good   example") == "example good a"

# leetcode submit region end(Prohibit modification and deletion)

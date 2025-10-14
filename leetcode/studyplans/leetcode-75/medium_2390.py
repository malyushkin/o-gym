# You are given a string s, which contains stars *.
#
#  In one operation, you can:
#
#
#  Choose a star in s.
#  Remove the closest non-star character to its left, as well as remove the
# star itself.
#
#
#  Return the string after all stars have been removed.
#
#  Note:
#
#
#  The input will be generated such that the operation is always possible.
#  It can be shown that the resulting string will always be unique.
#
#
#
#  Example 1:
#
#
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1ˢᵗ star is 't' in "leet**cod*e". s becomes
# "lee*cod*e".
# - The closest character to the 2ⁿᵈ star is 'e' in "lee*cod*e". s becomes
# "lecod*e".
# - The closest character to the 3ʳᵈ star is 'd' in "lecod*e". s becomes
# "lecoe".
# There are no more stars, so we return "lecoe".
#
#  Example 2:
#
#
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁵
#  s consists of lowercase English letters and stars *.
#  The operation above can be performed on s.
#
#
#  Related Topics String Stack Simulation 👍 3156 👎 230


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        letters = []

        while i < len(s):
            if s[i] == "*" and len(letters) > 0:
                letters.pop()
            else:
                letters.append(s[i])
            i += 1

        return "".join(letters)


s = Solution()
assert s.removeStars("leet**cod*e") == "lecoe"
assert s.removeStars("erase*****") == ""

# leetcode submit region end(Prohibit modification and deletion)

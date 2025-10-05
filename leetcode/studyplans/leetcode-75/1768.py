# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer than the
# other, append the additional letters onto the end of the merged string.
#
#  Return the merged string.
#
#
#  Example 1:
#
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
#
#  Example 2:
#
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
#
#
#  Example 3:
#
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
#
#  Constraints:
#
#
#  1 <= word1.length, word2.length <= 100
#  word1 and word2 consist of lowercase English letters.
#
#
#  Related Topics Two Pointers String 👍 4655 👎 136
from traceback import print_tb


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        pairs = zip(word1, word2)  # [Core] iterator
        pairs_len = 0
        result = ""

        for l1, l2 in pairs:
            result += l1
            result += l2
            pairs_len += 1

        result += word1[pairs_len:]  # [Core] slice (always safe)
        result += word2[pairs_len:]

        return result


task = Solution()
print(
    task.mergeAlternately("test1", "tes")
)

# leetcode submit region end(Prohibit modification and deletion)

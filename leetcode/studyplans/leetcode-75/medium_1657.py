# Two strings are considered close if you can attain one from the other using
# the following operations:
#
#
#  Operation 1: Swap any two existing characters.
#
#
#
#  For example, abcde -> aecdb
#
#
#  Operation 2: Transform every occurrence of one existing character into
# another existing character, and do the same with the other character.
#
#  For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into
# a's)
#
#
#
#
#  You can use the operations on either string as many times as necessary.
#
#  Given two strings, word1 and word2, return true if word1 and word2 are close,
#  and false otherwise.
#
#
#  Example 1:
#
#
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
#
#
#  Example 2:
#
#
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in
# any number of operations.
#
#
#  Example 3:
#
#
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
#
#
#
#  Constraints:
#
#
#  1 <= word1.length, word2.length <= 10⁵
#  word1 and word2 contain only lowercase English letters.
#
#
#  Related Topics Hash Table String Sorting Counting 👍 4025 👎 346


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # Collect letter stats
        def collect_stats(word):
            letter_stat = {}

            for letter in word:
                if letter not in letter_stat:
                    letter_stat[letter] = 0
                letter_stat[letter] += 1

            return letter_stat

        letter_stat1, letter_stat2 = collect_stats(word1), collect_stats(word2)

        # Check keys and values
        return (
                (set(letter_stat1.keys()) == set(letter_stat2.keys())) &
                (sorted(letter_stat1.values(), reverse=True) == sorted(letter_stat2.values(), reverse=True))
        )


s = Solution()
assert s.closeStrings("abc", "bca") == True
assert s.closeStrings("a", "aa") == False
assert s.closeStrings("cabbba", "abbccc") == True
assert s.closeStrings("abbzzca", "babzzcz") == False
assert s.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff") == False

# Given a string s, reverse only all the vowels in the string and return it.
#
#  The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
# lower and upper cases, more than once.
#
#
#  Example 1:
#
#
#  Input: s = "IceCreAm"
#
#
#  Output: "AceCreIm"
#
#  Explanation:
#
#  The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes
# "AceCreIm".
#
#  Example 2:
#
#
#  Input: s = "leetcode"
#
#
#  Output: "leotcede"
#
#
#  Constraints:
#
#
#  1 <= s.length <= 3 * 10⁵
#  s consist of printable ASCII characters.
#
#
#  Related Topics Two Pointers String 👍 5132 👎 2844


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # ----------------------------------------------------------
        # 1st idea: naive method
        # ----------------------------------------------------------
        #
        # vowels = set("aeiou")  # [Core] better to use set instead of list
        # s_vowels = [l for l in s if l.lower() in vowels]
        # res = [] # [Core] better to use list instead of str
        #
        # for l in s:
        #
        #     if l.lower() in vowels:
        #         res.append(s_vowels.pop())
        #
        #     else:
        #         res.append(l)
        #
        # return "".join(res)

        # ----------------------------------------------------------
        # 2nd idea: 2-pointers solution
        # ----------------------------------------------------------

        vowels = set("aeiouAEIOU")
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)


s = Solution()
assert s.reverseVowels("IceCreAm") == "AceCreIm"
assert s.reverseVowels("leetcode") == "leotcede"

# leetcode submit region end(Prohibit modification and deletion)

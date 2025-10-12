# Given an array of integers arr, return true if the number of occurrences of
# each value in the array is unique or false otherwise.
#
#
#  Example 1:
#
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
# values have the same number of occurrences.
#
#  Example 2:
#
#
# Input: arr = [1,2]
# Output: false
#
#
#  Example 3:
#
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
#
#
#  Constraints:
#
#
#  1 <= arr.length <= 1000
#  -1000 <= arr[i] <= 1000
#
#
#  Related Topics Array Hash Table 👍 5444 👎 153


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        occ = {}
        for item in arr:
            if item not in occ:
                occ[item] = 0
            occ[item] += 1

        return len(list(occ.values())) == len(list(set(occ.values())))


s = Solution()
assert s.uniqueOccurrences([1, 2, 2, 1, 1, 3]) == True
assert s.uniqueOccurrences([1, 2]) == False

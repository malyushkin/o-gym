# Given an integer array nums, return true if there exists a triple of indices (
# i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#
#
#  Example 2:
#
#
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
#
#
#  Example 3:
#
#
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 <
# nums[4] == 4 < nums[5] == 6.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 5 * 10⁵
#  -2³¹ <= nums[i] <= 2³¹ - 1
#
#
#
# Follow up: Could you implement a solution that runs in
# O(n) time complexity and
# O(1) space complexity?
#
#  Related Topics Array Greedy 👍 8670 👎 675


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float("inf")
        second = float("inf")

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True

        return False


s = Solution()
assert s.increasingTriplet([1, 2, 3, 4, 5]) == True
assert s.increasingTriplet([5, 4, 3, 2, 1]) == False
assert s.increasingTriplet([2, 1, 5, 0, 4, 6]) == True
assert s.increasingTriplet([20, 100, 10, 12, 5, 13]) == True

# leetcode submit region end(Prohibit modification and deletion)

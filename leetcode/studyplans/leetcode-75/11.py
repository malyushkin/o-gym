# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]).
#
#
#  Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
#  Return the maximum amount of water a container can store.
#
#  Notice that you may not slant the container.
#
#
#  Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
# 3,7]. In this case, the max area of water (blue section) the container can
# contain is 49.
#
#
#  Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
#
#  Constraints:
#
#
#  n == height.length
#  2 <= n <= 10⁵
#  0 <= height[i] <= 10⁴
#
#
#  Related Topics Array Two Pointers Greedy 👍 32738 👎 2100


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # ----------------------------------------------------------
        # 1st idea: naive method (O(n^2))
        # ----------------------------------------------------------
        #
        # i = 0
        # max_water = float("-inf")
        #
        # while i < len(height) - 1:
        #     h1 = height[i]
        #     j = i + 1
        #
        #     while j < len(height):
        #         h2 = height[j]
        #         width = j - i
        #         max_water = max(width * min(h1, h2), max_water)
        #         j += 1
        #
        #     i += 1
        #
        # return max_water

        # ----------------------------------------------------------
        # 2nd idea: two pointers
        # ----------------------------------------------------------

        i, j = 0, len(height) - 1
        max_water = float("-inf")

        while i < j:
            h = min(height[i], height[j])
            width = j - i
            max_water = max(max_water, h * width)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        # print(max_water)
        return max_water


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea([1, 1]) == 1

# You are given an integer array nums consisting of n elements, and an integer
# k.
#
#  Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10⁻⁵ will be accepted.
#
#
#  Example 1:
#
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
#
#  Example 2:
#
#
# Input: nums = [5], k = 1
# Output: 5.00000
#
#
#
#  Constraints:
#
#
#  n == nums.length
#  1 <= k <= n <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#
#
#  Related Topics Array Sliding Window 👍 4094 👎 374


# leetcode submit region begin(Prohibit modification and deletion)

import ast


def read_case(path):
    with open(path, "r", encoding="utf-8") as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
    try:
        nums = ast.literal_eval(line1)
        k = int(line2)
    except Exception as e:
        raise ValueError(f"Bad test file format: {e}")
    return nums, k


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum * 1.0 / k


s = Solution()

file_case_nums, file_case_k = read_case("643_test")

assert s.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4) == 12.75000
assert s.findMaxAverage(nums=[5], k=1) == 5.0
assert s.findMaxAverage(nums=[-1], k=1) == -1.0
assert s.findMaxAverage(nums=file_case_nums, k=file_case_k) == 105.31081896031841

# leetcode submit region end(Prohibit modification and deletion)

# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
#  Note that you must do this in-place without making a copy of the array.
#
#
#  Example 1:
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#  Example 2:
#  Input: nums = [0]
# Output: [0]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -2³¹ <= nums[i] <= 2³¹ - 1
#
#
#
# Follow up: Could you minimize the total number of operations done?
#
#  Related Topics Array Two Pointers 👍 18549 👎 553


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1

        while i >= 0:
            if nums[i] == 0:
                ij = i
                j = i + 1
                while j < len(nums):
                    nums[ij], nums[j] = nums[j], nums[ij]
                    ij += 1
                    j += 1
            i -= 1

        print(nums)
        return nums


s = Solution()
assert s.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert s.moveZeroes([0]) == [0]
assert s.moveZeroes([0, 0, 1]) == [1, 0, 0]

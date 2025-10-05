# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
#
#  Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return true if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule and false
# otherwise.
#
#
#  Example 1:
#  Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#
#  Example 2:
#  Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
#  Constraints:
#
#
#  1 <= flowerbed.length <= 2 * 10⁴
#  flowerbed[i] is 0 or 1.
#  There are no two adjacent flowers in flowerbed.
#  0 <= n <= flowerbed.length
#
#
#  Related Topics Array Greedy 👍 7161 👎 1299


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return True

        # edges
        if sum(flowerbed[:2]) == 0:
            flowerbed[0] = 1
            n -= 1
            if n == 0:
                return True

        if sum(flowerbed[-2:]) == 0:
            flowerbed[-1] = 1
            n -= 1
            if n == 0:
                return True

        # middle
        prev_neighbor = flowerbed[0]
        i = 1

        while i < len(flowerbed) - 1:
            next_neighbor = flowerbed[i + 1]

            if ((prev_neighbor + next_neighbor) == 0) and (flowerbed[i] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

            prev_neighbor = flowerbed[i]
            i += 1

        return False


s = Solution()
assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
assert s.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
assert s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False
assert s.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 1) == False
assert s.canPlaceFlowers([0, 0, 1, 0, 1], 1) == True
assert s.canPlaceFlowers([0, 0, 1, 0, 0], 1) == True
assert s.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0) == True

# leetcode submit region end(Prohibit modification and deletion)

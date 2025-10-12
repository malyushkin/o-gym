# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri,
# cj) such that row ri and column cj are equal.
#
#  A row and column pair is considered equal if they contain the same elements
# in the same order (i.e., an equal array).
#
#
#  Example 1:
#
#
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
#
#
#  Example 2:
#
#
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
#
#
#
#  Constraints:
#
#
#  n == grid.length == grid[i].length
#  1 <= n <= 200
#  1 <= grid[i][j] <= 10⁵
#
#
#  Related Topics Array Hash Table Matrix Simulation 👍 2444 👎 183


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i, j = 0, 0
        grid_stats = {}

        while j < len(grid):
            # verticals
            vert_values = []
            while i < len(grid):
                vert_values.append(grid[i][j])
                i += 1

            vert = "-".join([str(l) for l in vert_values])

            if vert not in grid_stats:
                grid_stats[vert] = [0, 1]
            else:
                grid_stats[vert][1] += 1

            # horizontals
            hort = "-".join([str(l) for l in grid[j]])
            if hort not in grid_stats:
                grid_stats[hort] = [1, 0]
            else:
                grid_stats[hort][0] += 1

            i = 0
            j += 1

        print(grid_stats.values())

        return sum([pair[0] * pair[1] for pair in grid_stats.values() if sum(pair) > 1])


s = Solution()

assert s.equalPairs([
    [3, 2, 1],
    [1, 7, 6],
    [2, 7, 7],
]) == 1
#
assert s.equalPairs([
    [3, 1, 2, 2],
    [1, 4, 4, 5],
    [2, 4, 2, 2],
    [2, 4, 2, 2],
]) == 3

assert s.equalPairs([
    [13, 13],
    [13, 13]
]) == 4

assert s.equalPairs([
    [11, 1],
    [1, 11]
]) == 2

assert s.equalPairs([
    [17, 13, 7, 5, 5, 11, 10, 16, 5],
    [5, 3, 3, 3, 3, 3, 12, 3, 3],
    [5, 3, 3, 3, 3, 3, 12, 3, 3],
    [17, 10, 1, 3, 3, 9, 10, 11, 3],
    [5, 3, 3, 3, 3, 3, 12, 3, 3],
    [5, 3, 3, 3, 3, 3, 12, 3, 3],
    [10, 9, 15, 12, 12, 19, 18, 16, 12],
    [5, 3, 3, 3, 3, 3, 12, 3, 3],
    [1, 2, 17, 3, 3, 11, 19, 9, 3]
]) == 15

# leetcode submit region end(Prohibit modification and deletion)

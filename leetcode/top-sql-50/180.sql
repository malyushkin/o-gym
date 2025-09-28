-- #
-- Table: Logs
-- #
-- #
-- # +-------------+---------+
-- # | Column Name | Type    |
-- # +-------------+---------+
-- # | id          | int     |
-- # | num         | varchar |
-- # +-------------+---------+
-- # In SQL, id is the primary key for this table.
-- # id is an autoincrement column starting from 1.
-- #
-- #
-- #
-- #
-- #  Find all numbers that appear at least three times consecutively.
-- #
-- #  Return the result table in any order.
-- #
-- #  The result format is in the following example.
-- #
-- #
-- #  Example 1:
-- #
-- #
-- # Input:
-- # Logs table:
-- # +----+-----+
-- # | id | num |
-- # +----+-----+
-- # | 1  | 1   |
-- # | 2  | 1   |
-- # | 3  | 1   |
-- # | 4  | 2   |
-- # | 5  | 1   |
-- # | 6  | 2   |
-- # | 7  | 2   |
-- # +----+-----+
-- # Output:
-- # +-----------------+
-- # | ConsecutiveNums |
-- # +-----------------+
-- # | 1               |
-- # +-----------------+
-- # Explanation: 1 is the only number that appears consecutively for at least
-- # three times.
-- #
-- #
-- #  Related Topics Database
-- # 👍 2548
-- # 👎 350

SELECT DISTINCT t.num AS "ConsecutiveNums"
FROM (SELECT num,
             LAG(num, 1) OVER (ORDER BY id) AS "prev", LAG(num, 2) OVER (ORDER BY id) AS "prev2"
      FROM Logs) AS t
WHERE t.num = t.prev
  AND t.num = t.prev2

-- # There is no code of Python type for this problem
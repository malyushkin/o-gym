-- # Table: Products
-- #
-- #
-- # +---------------+---------+
-- # | Column Name   | Type    |
-- # +---------------+---------+
-- # | product_id    | int     |
-- # | new_price     | int     |
-- # | change_date   | date    |
-- # +---------------+---------+
-- # (product_id, change_date) is the primary key (combination of columns with
-- # unique values) of this table.
-- # Each row of this table indicates that the price of some product was changed
-- # to a new price at some date.
-- #
-- #  Initially, all products have price 10.
-- #
-- #  Write a solution to find the prices of all products on the date 2019-08-16.
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
-- # Products table:
-- # +------------+-----------+-------------+
-- # | product_id | new_price | change_date |
-- # +------------+-----------+-------------+
-- # | 1          | 20        | 2019-08-14  |
-- # | 2          | 50        | 2019-08-14  |
-- # | 1          | 30        | 2019-08-15  |
-- # | 1          | 35        | 2019-08-16  |
-- # | 2          | 65        | 2019-08-17  |
-- # | 3          | 20        | 2019-08-18  |
-- # +------------+-----------+-------------+
-- # Output:
-- # +------------+-------+
-- # | product_id | price |
-- # +------------+-------+
-- # | 2          | 50    |
-- # | 1          | 35    |
-- # | 3          | 10    |
-- # +------------+-------+
-- #
-- #
-- #  Related Topics Database 👍 1262 👎 301
-- # There is no code of Python type for this problem

WITH last_change AS (SELECT product_id,
                            MAX(change_date) AS max_change_date
                     FROM Products
                     WHERE change_date <= DATE '2019-08-16'
                     GROUP BY product_id),
     last_price AS (SELECT p.product_id, p.new_price
                    FROM Products p
                             JOIN last_change lc
                                  ON lc.product_id = p.product_id
                                      AND lc.max_change_date = p.change_date),
     all_products AS (SELECT DISTINCT product_id
                      FROM Products)
SELECT ap.product_id,
       COALESCE(lp.new_price, 10) AS price
FROM all_products ap
         LEFT JOIN last_price lp
                   ON lp.product_id = ap.product_id
-- SQL Question 2: Analyzing Ratings For Netflix Shows
-- Given a table of user ratings for Netflix shows, calculate the average rating for each show within a given month.
-- Assume that there is a column for user id, show id, rating (out of 5 stars), and date of review. Order the results
-- by month and then by average rating (descending order).
--
-- This is will provide an interesting insights into how show ratings fluctuate over time and which shows have
-- garnered the most positive feedback.
--
-- Sample Tables:
--
-- show_reviews Example Input:
-- review_id	user_id	review_date	show_id	stars
-- 6171	123	06/08/2022 00:00:00	50001	4
-- 7802	265	06/10/2022 00:00:00	69852	4
-- 5293	362	06/18/2022 00:00:00	50001	3
-- 6352	192	07/26/2022 00:00:00	69852	3
-- 4517	981	07/05/2022 00:00:00	69852	2

-- Example Output:
-- mth	show_id	avg_stars
-- 6	50001	3.50
-- 6	69852	4.00
-- 7	69852	2.50

SELECT
    date_trunc('month', review_date) AS "mth",
    show_id,
    ROUND(AVG(stars), 2) AS "avg_stars"
FROM
    show_reviews
GROUP BY
    1, 2
ORDER BY
    1, 2 DESC

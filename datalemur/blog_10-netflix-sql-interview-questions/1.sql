-- SQL Question 1: Identify VIP Users for Netflix
-- To better cater to its most dedicated users, Netflix would like to identify its "VIP users" - those who are most
-- active in terms of the number of hours of content they watch. Write a SQL query that will retrieve the top 10 users
-- with the most watched hours in the last month.
--
-- users Example Input Table
-- user_id	sign_up_date	subscription_type
-- 435	08/20/2020	Standard
-- 278	01/01/2021	Premium
-- 529	09/15/2021	Basic
-- 692	12/28/2021	Standard
-- 729	01/06/2022	Premium
--
-- watching_activity Example Input Table
-- activity_id	user_id	date_time	show_id	hours_watched
-- 10355	435	02/09/2022 12:30:00	12001	2.5
-- 14872	278	02/10/2022 14:15:00	17285	1.2
-- 12293	529	02/18/2022 21:10:00	12001	4.3
-- 16352	692	02/20/2022 19:00:00	17285	3.7
-- 17485	729	02/25/2022 16:45:00	17285	1.9

SELECT
    user_id,
    SUM(hours_watched)
FROM
    watching_activity
WHERE
    date_time >= date_trunc('month', CURRENT_DATE - INTERVAL '1 month')
    AND date_time < date_trunc('month', CURRENT_DATE)
GROUP BY
    user_id
ORDER BY
    2 DESC
LIMIT
    10;
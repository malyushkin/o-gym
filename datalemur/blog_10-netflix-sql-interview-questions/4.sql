-- SQL Question 4: Filter Netflix Users Based on Viewing History and Subscription Status
-- You are given a database of Netflix's user viewing history and their current subscription status. Write a SQL query
-- to find all active customers who watched more than 10 episodes of a show called "Stranger Things" in the last 30
-- days.
--
-- For this question, consider the following tables:
--
-- users Example Input:
-- user_id	active
-- 1001	true
-- 1002	false
-- 1003	true
-- 1004	true
-- 1005	false
--
-- viewing_history Example Input:
-- user_id	show_id	episode_id	watch_date
-- 1001	2001	3001	2022-10-01
-- 1001	2001	3002	2022-10-02
-- 1001	2001	3003	2022-10-03
-- 1002	2001	3001	2022-10-01
-- 1002	2001	3002	2022-10-02
-- 1003	2001	3001	2022-10-01
-- 1003	2001	3002	2022-11-01
-- 1003	2001	3003	2022-11-02
-- 1004	2002	3004	2022-11-03


WITH active_users AS (
    SELECT user_id
    FROM users
    WHERE active IS true
)
SELECT
    vh.user_id
FROM
    viewing_history vh
INNER JOIN
    active_users au ON au.user_id = vh.user_id
WHERE
    watch_date >= CURRENT_DATE - INTERVAL '30 day'
    AND vh.show_id = 2001
GROUP BY
    vh.user_id
HAVING
    COUNT(DISTINCT episode_id) > 10
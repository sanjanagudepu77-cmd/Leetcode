# Write your MySQL query statement below
SELECT a.user_id,round((avg(case when action='confirmed'then 1 else 0 end)),2) AS confirmation_rate
FROM Signups a
LEFT JOIN Confirmations b
ON a.user_id=b.user_id
GROUP BY user_id;

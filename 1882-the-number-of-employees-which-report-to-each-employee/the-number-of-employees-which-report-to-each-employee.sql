# Write your MySQL query statement below
SELECT a.employee_id, a.name, COUNT(b.employee_id) as reports_count, ROUND(AVG(b.age)) AS average_age
FROM Employees b 
JOIN employees a
ON b.reports_to = a.employee_id
GROUP BY employee_id
ORDER BY employee_id

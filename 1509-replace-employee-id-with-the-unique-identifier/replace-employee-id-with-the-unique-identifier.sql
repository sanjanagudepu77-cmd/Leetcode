# Write your MySQL query statement below
SELECT unique_id,name
FROM Employees t
LEFT JOIN EmployeeUNI u
ON t.id=u.id;

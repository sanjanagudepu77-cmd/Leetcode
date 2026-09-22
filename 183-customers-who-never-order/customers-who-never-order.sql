# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers c LEFT JOIN Orders o 
ON c.id = o.customerId
WHERE O.customerId IS NULL;



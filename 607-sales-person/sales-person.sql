# Write your MySQL query statement below
select s.name
from SalesPerson s
where s.name not in
(select s.name
from salesperson as s
left join orders o on s.sales_id=o.sales_id
left join company c on c.com_id=o.com_id
where c.name='red')
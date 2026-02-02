# Write your MySQL query statement below
select 
    P.project_id,
    round(avg(E.experience_years),2) as average_years
from Employee E 
join Project P using(employee_id)
group by P.Project_id


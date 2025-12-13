select e.name , e1.unique_id
from Employees as e
left join EmployeeUNI as e1 t
on e.id=e1.id;

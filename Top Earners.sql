select max(months*salary) as earning, count(*)
from employee
where months*salary = (select max(months*salary) from employee)

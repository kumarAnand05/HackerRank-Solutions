select concat(name, '(', left(occupation,1), ')') as acc
from occupations

union all 

select concat('There are a total of ', count(*),' ', lower(occupation),'s.') as acc
from occupations group by occupation

order by acc

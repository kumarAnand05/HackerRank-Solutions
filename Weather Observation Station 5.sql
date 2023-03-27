(select city, length(city) l
from station
order by l asc, city
limit 1)
union
(select city, length(city) l
from station
order by l desc, city
limit 1)

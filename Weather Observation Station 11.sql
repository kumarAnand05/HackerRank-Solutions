select distinct(city) from station
where right(city,1) not in ('a','e','i','o','u') or left(city,1) not in ('a','e','i','o','u')

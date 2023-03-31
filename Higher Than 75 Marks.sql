select name from students
where marks>75
order by substring(name,-3,3), id

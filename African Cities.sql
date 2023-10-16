/*
Question:

Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format

The CITY and COUNTRY tables are described as follows:

*/

--Solution:

select city.name from city
join country
on CITY.CountryCode = COUNTRY.Code
where country.continent = 'Africa'

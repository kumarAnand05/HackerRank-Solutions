SELECT
CASE
    WHEN A+B<=C or A+C<=B OR B+C<=A THEN 'Not A Triangle'
    WHEN A=B and B=C THEN 'Equilateral'
    WHEN A = B or A = C or B = C THEN 'Isosceles'    
    Else 'Scalene'
End as result
FROM Triangles;

SELECT c.company_code, c.founder,COUNT(DISTINCT lm.lead_manager_code ), COUNT(DISTINCT sm.senior_manager_code ), COUNT(DISTINCT m.manager_code ), COUNT(DISTINCT e.employee_code )
FROM company AS c
JOIN lead_manager AS lm
ON c.company_code = lm.company_code
JOIN senior_manager AS sm
ON lm.company_code = sm.company_code
JOIN manager as m
ON sm.company_code = m.company_code
JOIN employee as e
ON m.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;

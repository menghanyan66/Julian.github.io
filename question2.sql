SELECT d.dept_name, e.emp_name, e.emp_salary 
FROM Employee e
INNER JOIN Department d ON e.dept_id = d.dept_id
WHERE (e.dept_id, e.emp_salary) IN
   (SELECT dept_id, MAX(emp_salary) 
    FROM Employee 
    GROUP BY dept_id)
ORDER BY d.dept_name ASC;

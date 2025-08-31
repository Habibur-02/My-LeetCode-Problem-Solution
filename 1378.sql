SELECT
    e2.unique_id AS unique_id,
    e1.name AS name
FROm
    Employees AS e1
LEFT JOIN
    EmployeeUNI AS e2
    USING(id);
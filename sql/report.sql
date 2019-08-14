SELECT CASE 
    WHEN T.Grade >= 8 THEN T.Name
    ELSE NULL
END, T.Grade, T.Marks
FROM
(
    SELECT Students.Name, Grades.Grade, Students.Marks
    FROM Students
    INNER JOIN Grades
    ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark
    ORDER BY Grades.Grade DESC, Students.Name ASC
) AS T

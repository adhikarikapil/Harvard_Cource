SET
    SQL_SAFE_UPDATES = 0;

CREATE TABLE
    student (
        Rollno INT PRIMARY KEY,
        Name VARCHAR(50),
        Marks INT NOT NULL,
        Grade VARCHAR(10),
        City VARCHAR(30)
    );

INSERT INTO
    student (Rollno, Name, Marks, Grade, City)
VALUES
    (101, "Anil", 78, "C", "Pune"),
    (102, "Bhumeka", 93, "A", "Mumbai"),
    (103, "Chetan", 85, "B", "Mumbai"),
    (104, "Dhruv", 96, "A", "Delhi"),
    (105, "Emanuel", 12, "F", "Delhi"),
    (106, "Farah", 82, "B", "Delhi");

SELECT
    *
FROM
    student
ORDER BY
    Marks ASC;

SELECT
    City,
    count(Rollno)
FROM
    student
GROUP BY
    (city);

SELECT
    city,
    avg(Marks)
FROM
    student
GROUP BY
    city
ORDER BY
    AVG(Marks) ASC;

SELECT
    city,
    count(Rollno)
FROM
    student
GROUP BY
    City
HAVING
    max(Marks) > 90;

UPDATE student
SET
    Grade = "F"
WHERE
    Grade = "Fail";

ALTER TABLE student
ADD COLUMN Age;

SELECT
    *
FROM
    student;

ALTER TABLE student
DROP COLUMN Age;

CREATE TABLE
    payment (
        customer_id INT PRIMARY KEY,
        customer VARCHAR(50),
        mode VARCHAR(30),
        city VARCHAR(30)
    );

INSERT INTO
    payment (customer_id, customer, mode, city)
VALUES
    (101, "Olivia Barret", "Netbanking", "Portland"),
    (102, "Ethan Sinclair", "Credit Card", "Miami"),
    (103, "Maya Hernandez", "Credit Card", "Seattle"),
    (104, "Liam Donovan", "Netbanking", "Denver"),
    (105, "Sopia Nguyen", "Credit Card", "New Orleans"),
    (106, "Celeb Foster", "Debit Card", "Minneapolis"),
    (107, "Ava Patel", "Debit Card", "Phoenix"),
    (108, "Lucas Carter", "Netbanking", "Boston"),
    (
        109,
        "Isabella Martinez",
        "Netbanking",
        "Nashville"
    ),
    (110, "Jackson Brooks", "Credit Card", "Boston");

SELECT
    *
FROM
    payment;

SELECT
    mode,
    count(mode)
FROM
    payment
GROUP BY
    mode;

DROP TABLE payment;

CREATE TABLE
    dept (id INT PRIMARY KEY, name VARCHAR(50));

INSERT INTO
    dept (id, name)
VALUES
    (101, "English"),
    (102, "It");

UPDATE dept
SET
    id = 103
WHERE
    name = "It";

CREATE TABLE
    teacher (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        dept_id INT,
        FOREIGN KEY (dept_id) REFERENCES dept (id) ON DELETE CASCADE ON UPDATE CASCADE
    );

INSERT INTO
    teacher (id, name, dept_id)
VALUES
    (101, "Kapil", 102),
    (102, "Samip", 103);

SELECT
    *
FROM
    dept;

SELECT *
FROM student as s 
LEFT JOIN dept as d  
ON s.Rollno = d.id
UNION
SELECT *
FROM student as s 
RIGHT JOIN dept as d
ON s.Rollno = d.id;

SELECT *
FROM student as s 
JOIN student as stu 
ON s.Rollno = stu.Rollno;


SELECT Rollno, Name, Marks FROM student
WHERE Marks > (SELECT avg(marks) FROM student);

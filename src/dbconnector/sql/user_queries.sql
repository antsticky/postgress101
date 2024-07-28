-- Select all columns from all rows
SELECT
  *
FROM
  users;

-- Select specific columns (name and position) from all rows
SELECT
  name,
  position
FROM
  users;

-- Select all users who are at least 25 years old
SELECT
  *
FROM
  users
WHERE
  age >= 25;
  

-- Select all users and order by age in ascending order
SELECT
  *
FROM
  users
ORDER BY
  age ASC;

-- Select the top 5 oldest users
SELECT
  *
FROM
  users
ORDER BY
  age DESC
LIMIT
  5;

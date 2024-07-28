CREATE OR REPLACE FUNCTION SelectUserByAge(age_limit INTEGER, name_lookup VARCHAR(255))
RETURNS TABLE(id INT, name VARCHAR, age INT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM users WHERE users.name = name_lookup AND users.age > age_limit;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM SelectUserByAge(10, "Alice Johnson");
DROP FUNCTION IF EXISTS SelectUserByAge(INTEGER, VARCHAR);

CREATE OR REPLACE FUNCTION SelectUserByAge(age_limit INTEGER, name_lookup VARCHAR(255))
RETURNS SETOF users AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM users WHERE users.name = name_lookup AND users.age > age_limit;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM SelectUserByAge(10, 'Alice Johnson');
-- creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS INT BEGIN
DECLARE s INT;
IF b = 0 THEN
SET s = 0
  ELSE
SET s = a / b RETURN s;
ENDIF;
END
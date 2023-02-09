-- Create a trigger that decreases the quantity of an item after adding a new order
DELIMITER //
CREATE TRIGGER `del_item`
AFTER INSERT ON `holberton`.`items` 
FOR EACH ROW 
  BEGIN
    INSERT INTO `holberton`.`orders`
    SET NEW.quantity = NEW.quantity - 1;
  END //

DELIMITER ;

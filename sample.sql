CREATE PROCEDURE `alter_attack_growth` ()
BEGIN
  DECLARE temp_id INT;
  DECLARE temp_growth, temp_max, temp_start, temp_diff FLOAT ;

  DECLARE done INT DEFAULT false;
  DECLARE cur_hero CURSOR FOR SELECT id, attack_growth, attack_max, attack_start FROM heros;
  DECLARE continue handler FOR NOT FOUND SET done = true ;

  OPEN cur_hero;
  FETCH cur_hero INTO temp_id, temp_growth, temp_max, temp_start;
  REPEAT
    IF NOT done THEN
      SET temp_diff = temp_max - temp_start;
      IF temp_growth < 5 THEN
        IF temp_diff > 200 THEN
          SET temp_growth = temp_growth * 1.1;
        else if temp_diff >= 150 AND temp_diff <= 200 THEN
          SET temp_growth = temp_growth * 1.08;
        ELSE IF temp_diff < 150 THEN
          SET temp_growth = temp_growth * 1.07 THEN
        END IF ;
      ELSE IF temp_growth >= 5 AND temp_growth <= 10 then
        SET temp_growth = temp_growth * 1.05;
      END IF;
      UPDATE heros SET attack_growth = ROUND(temp_growth, 3) Where id = temp_id;
    END IF;
  FETCH cur_hero INTO temp_id , temp_growth, temp_max, temp_start;
  UNTIL done = true END REPEAT;
  CLOSE cur_hero;
END


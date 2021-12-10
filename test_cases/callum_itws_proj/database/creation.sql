DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS accounts;

-- Here are commands for creating the tables in the MySQL database.
-- The code expects these tables to exist in a database named `cooking`
CREATE TABLE `accounts` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(32) NOT NULL,
  `password` VARCHAR(255) BINARY NOT NULL,
  `privilege` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY (`username`)
);

CREATE TABLE `recipes` (
  `recipe_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `instructions` TEXT NOT NULL, -- This stores ~64kb for the instruction text. 
                                -- Does put a maximum character count on recipes
  `title` VARCHAR(40) NOT NULL, -- 40 characters should be enough for a title.
  `user_id` INT UNSIGNED NOT NULL,
  `submitted_date` DATE NOT NULL DEFAULT CURRENT_DATE,
  PRIMARY KEY(`recipe_id`),
  FOREIGN KEY (`user_id`) REFERENCES `accounts` (`user_id`)
);

-- Creating the tag table
CREATE TABLE tags (
  recipe_id INT UNSIGNED NOT NULL,
  tag_value varchar(20) NOT NULL,
  PRIMARY KEY(recipe_id, tag_value),
  FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`)
);

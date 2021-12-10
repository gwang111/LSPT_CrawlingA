# Lab 10

## Description

In this lab we imported a MySQL database, added actors to a table, created a movies table and added movies to it, and created a relationship table between movies and actors. We also created another page to view the movies in the table that we created. Overall, this lab was pretty simple. I'm somewhat familar with databases, but I got some good practice with SQL statements. It was more tedious than difficult to create the page to add/remove/view movies. It was very similar to the actors page, so most of the code was easily ported over. I still think this was an important lab, though. It makes sure we all know how to interact with databases so that we can use them in a basic sense for our final projects, and also makes it easier to learn more in future classes.

## MySQL Commands

### Create Actors Table + Adding Actors

```sql
CREATE TABLE `actors` (
 `actorid` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `first_names` varchar(100) NOT NULL,
 `last_name` varchar(100) NOT NULL,
 `dob` DATE NOT NULL,
 PRIMARY KEY (`actorid`)
);

INSERT INTO `actors` (`actorid`, `first_names`, `last_name`, `dob`) VALUES (NULL, 'Leonardo', 'DiCaprio', '1974-11-11');
INSERT INTO `actors` (`actorid`, `first_names`, `last_name`, `dob`) VALUES (NULL, 'Denzel', 'Washington', '1954-12-28');
INSERT INTO `actors` (`actorid`, `first_names`, `last_name`, `dob`) VALUES (NULL, 'Nicolas', 'Coppola', '1964-01-07');
INSERT INTO `actors` (`actorid`, `first_names`, `last_name`, `dob`) VALUES (NULL, 'Tom', 'Cruise', '1962-07-03');
INSERT INTO `actors` (`actorid`, `first_names`, `last_name`, `dob`) VALUES (NULL, 'Morgan', 'Freeman', '1937-06-01');
```

### List all actors born on or after 1960

``` sql
SELECT * FROM `actors` WHERE `dob` >= '1960-01-01'
```

### Create Movie/Actor Relations Table

``` sql
CREATE TABLE `relationships` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `movieid` int unsigned NOT NULL,
 `actorid` int unsigned NOT NULL,
 PRIMARY KEY (`id`),
 FOREIGN KEY (movieid) REFERENCES movies(movieid),
 FOREIGN KEY (actorid) REFERENCES actors(actorid)
);

INSERT INTO `movies` (`title`, `year`) VALUES ('Oblivion', '2013');
INSERT INTO `movies` (`title`, `year`) VALUES ('The Equalizer', '2014');
INSERT INTO `movies` (`title`, `year`) VALUES ('National Treasure', '2004');
INSERT INTO `movies` (`title`, `year`) VALUES ('The Wolf of Wall Street', '2013');
INSERT INTO `movies` (`title`, `year`) VALUES ('Edge Of Tomorrow', '2014');


INSERT INTO `relationships` (`movieid`, `actorid`) VALUES (6, 4);
INSERT INTO `relationships` (`movieid`, `actorid`) VALUES (6, 5);
INSERT INTO `relationships` (`movieid`, `actorid`) VALUES (7, 2);
INSERT INTO `relationships` (`movieid`, `actorid`) VALUES (8, 3);
INSERT INTO `relationships` (`movieid`, `actorid`) VALUES (9, 1);
INSERT INTO `relationships` (`movieid`, `actorid`) VALUES (10, 4);
```

CREATE DATABASE IF NOT EXISTS tobid;

USE tobid;

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  role VARCHAR(45), 
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS attractions (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    description VARCHAR(45) NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS courses (
    id INT NOT NULL AUTO_INCREMENT,
    tourist_id INT,
    title VARCHAR(255),
    category VARCHAR(255),
    reservation_time DATETIME,
    status VARCHAR(45) DEFAULT 'Active',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS course_cost (
  id INT NOT NULL AUTO_INCREMENT,
  driver_id INT,
  course_id INT,
  cost FLOAT,
  is_selected BOOLEAN DEFAULT false,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS course_attractions (
  id INT NOT NULL AUTO_INCREMENT,
  course_id INT,
  attraction_id INT,
  order_num INT,
  is_last BOOLEAN,
  departure_time TIMESTAMP,
  PRIMARY KEY (id)
);


ALTER TABLE `courses` ADD FOREIGN KEY (`tourist_id`) REFERENCES `users` (`id`); 

ALTER TABLE `course_attractions` ADD FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`);

ALTER TABLE `course_attractions` ADD FOREIGN KEY (`attraction_id`) REFERENCES `attractions` (`id`);

ALTER TABLE `course_cost` ADD FOREIGN KEY (`driver_id`) REFERENCES `users` (`id`);

ALTER TABLE `course_cost` ADD FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`);



-- 예시 데이터 


INSERT INTO users (`username`, `role`, `created_at`)
VALUES ('admin', 'admin', NOW()),
       ('tourist_user', 'tourist 1', NOW()),
       ('driver_user', 'driver 1', NOW()),
       ('tourist_user', 'tourist 2', NOW()),
       ('driver_user', 'driver 2', NOW());


INSERT INTO attractions (name, description, created_at)
VALUES
    ('Attraction 1', 'Description 1', '2023-08-19 10:00:00'),
    ('Attraction 2', 'Description 2', '2023-08-19 11:15:00'),
    ('Attraction 3', 'Description 3', '2023-08-19 12:30:00'),
    ('Attraction 4', 'Description 4', '2023-08-19 14:45:00'),
    ('Attraction 5', 'Description 5', '2023-08-19 16:00:00');


INSERT INTO courses (tourist_id, title, category, reservation_time, status, created_at)
VALUES
(1, 'Tour 1', 'Family', '2023-08-20 10:00:00', 'ACTIVE', NOW()),
(2, 'Tour 2', 'Alone', '2023-08-21 14:30:00', 'ACTIVE', NOW()),
(2, 'Tour 3', 'Couple', '2023-08-22 09:15:00', 'INACTIVE', NOW()),
(4, 'Tour 3', 'Relaxed', '2023-08-22 09:15:00', 'INACTIVE', NOW()),
(4, 'Tour 4', 'HotPlace', '2023-08-23 11:45:00', 'ACTIVE', NOW());


INSERT INTO course_attractions (course_id, attraction_id, order_num, is_last, departure_time)
VALUES
(1, 1, 1, false, '2023-08-20 10:00:00'),
(1, 2, 2, true, '2023-08-20 12:00:00'),
(2, 3, 2, true, '2023-08-20 12:00:00'),
(2, 4, 1, true, '2023-08-20 12:00:00');


INSERT INTO course_cost (driver_id, course_id, cost)
VALUES
(3, 2, 45000),
(5, 2, 20000),
(3, 4, 100000),
(5, 4, 7000),
(3, 4, 5000),
(5, 4, 2000);
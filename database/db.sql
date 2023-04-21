-- Db scripts
-- --------------------------------------------------------
CREATE DATABASE IF NOT EXISTS `earthquakes`;
        
USE earthquakes;
--
-- Table earthquakes script
--
CREATE TABLE earthquakes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    magnitude FLOAT NOT NULL,
    location VARCHAR(500) NOT NULL,
    time DATETIME NOT NULL
);
--
-- Table cities script
--
CREATE TABLE cities (
  id INT NOT NULL AUTO_INCREMENT,
  city VARCHAR(255) NOT NULL,
  latitude DECIMAL(10, 7) NOT NULL,
  longitude DECIMAL(10, 7) NOT NULL,
  PRIMARY KEY (id)
);
--
-- Insert initials cities script
--
INSERT INTO cities (city, latitude, longitude) VALUES ('Los Angeles', 34.0522, -118.2437);

INSERT INTO cities (city, latitude, longitude) VALUES ('San Francisco', 37.7749, -122.4194);

INSERT INTO cities (city, latitude, longitude) VALUES ('Tokyo', 35.6762, 139.6503);


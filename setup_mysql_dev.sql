-- A script that Prepares a MySQL server for the project.

-- Create or use the database if it already exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or use the user if it already exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user on the specified databases
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Show the grants for the user at the end for verification
SHOW GRANTS FOR 'hbnb_dev'@'localhost';

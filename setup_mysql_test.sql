-- A script that Prepares a MySQL Test server for the project.

-- Create or use the database if it already exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or use the user if it already exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user on the specified databases
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Show the grants for the user at the end for verification
SHOW GRANTS FOR 'hbnb_test'@'localhost';

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Drop user if exists to ensure password is correct (optional but safe)
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Create user with password
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

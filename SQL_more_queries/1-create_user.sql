-- Drop user if exists to ensure password is correct
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create user with the required password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

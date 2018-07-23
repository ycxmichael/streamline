-- DROP EXISTING DATABASE
DROP TABLE IF EXISTS Listener_User_ID CASCADE;
DROP TABLE IF EXISTS Listener_Email;
DROP DATABASE IF EXISTS streamline_db;

DROP OWNED BY sl_admin;
DROP USER IF EXISTS sl_admin;



-- CREATE USER TO BE USED IN DJANGO
CREATE USER sl_admin WITH password '12345';
--ALTER ROLE sl_admin CREATEDB;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sl_admin;
-- CREATE DATABASE
CREATE DATABASE streamline_db;
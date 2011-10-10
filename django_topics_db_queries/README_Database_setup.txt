
First we need to create the database

$ mysql -u root -p

mysql > drop database mqueries;
mysql > create database mqueries
mysql > describe user;
mysql > create user 'mqueries'@'%' identified by 'mqueries';
mysql > show grants for mqueries;
mysql > grant Select, Insert, Update, Delete, Alter, Create, Index on mqueries.* to 'mqueries'@'%';

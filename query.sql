drop database if exists log;
create database log;
\c log;
create table logtable(
    id int primary key, 
    a int, 
    b int, 
    c int, 
    d int, 
    e int, 
    f int, 
    g int, 
    h int
);
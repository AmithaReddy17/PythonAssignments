##1##
CREATE DATABASE Hotel_Management_system;
create table Customers_H(
cust_ID int primary key,
cust_Nmae varchar(255),
cust_City varchar(255),
cust_Room_No int,
check_In_Date date
);

insert into Customers_H
(cust_ID,cust_Nmae,cust_City,cust_Room_No,check_In_date)
values
(1, 'Kev', 'PA', 101, "1997-06-17"),
(2, 'Malti', 'FL', 102, "1995-07-13"),
(3, 'Joe', 'OH', 103, "1994-01-3"),
(4, 'Ria', 'MI', 104, "1998-05-15"),
(5, 'Rose', 'NJ', 105, "1991-08-9");
SELECT * FROM Customers_H;




#3#

CREATE DATABASE E_Commerce_Website;
CREATE TABLE categories_E (
  CategoryID int(11) NOT NULL,
  CategoryName varchar(255) DEFAULT NULL,
  Description varchar(255) DEFAULT NULL
);




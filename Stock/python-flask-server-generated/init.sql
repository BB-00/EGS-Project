use stock_db;

create table materials (materials_ID int primary key, name varchar(30) ) ;

create table type (type_ID int primary key, name varchar(30));

create table providers (providers_ID int primary key, name varchar(30), country varchar(30), city varchar(30), ZIP int, address varchar(30), email varchar(30), site varchar(30), phone int);

create table products (product_ID int primary key, name varchar(30), size int, materials_ID int, CONSTRAINT foreign key (materials_ID) references materials (materials_ID), provider int, CONSTRAINT foreign key (provider) references providers (providers_ID), product_type int, CONSTRAINT foreign key (product_type) references type (type_ID), reference int, quantity int, buy_price int);

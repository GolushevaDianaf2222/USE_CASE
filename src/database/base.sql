create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    power_level integer
);

create table client(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
);

create table contract(
	id integer PRIMARY KEY autoincrement,
    date varchar(50),
    contract_number INTEGER,
    Project_name varchar(50),
    id_client integer,
    id_company integer
);

create table object(
    id     integer PRIMARY KEY autoincrement,
    address integer,
    id_client integer
);

create table Company(
    id     integer PRIMARY KEY autoincrement,
    name varchar(50),
    id_contract integer,
    id_working_hours integer,
    id_provider integer
);

create table working_hours(
    id     integer PRIMARY KEY autoincrement,
    getting_started integer,
    end_of_work integer,
    id_company integer
);

create table warehouse(
    id     integer PRIMARY KEY autoincrement,
    address integer,
    delivery_date integer,
    list_of_materials varchar(50),
    id_company integer,
    id_provider integer
);

create table provider(
    id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create table worker(
    id integer PRIMARY KEY autoincrement,
    name varchar(50),
    type_of_work varchar(50),
    id_working_hours integer,
    id_company integer
);

create table product(
    id integer PRIMARY KEY autoincrement,
    name varchar(50),
    price_product varchar(50),
    delivery_date varchar(50),
    id_provider integer
);

create table departments(
    id integer PRIMARY KEY autoincrement,
    department_name varchar(50),
    id_warehouse integer
);

create table positions(
    id integer PRIMARY KEY autoincrement,
    title_of_the_position varchar(50),
    id_provider integer,
    id_workers integer
);
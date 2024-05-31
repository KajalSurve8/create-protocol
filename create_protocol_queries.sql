use schema_1;
--------------------------------------------
select * from protocol_new;
truncate protocol_new;
--------------------------------------------
select * from test_list_master;
-- Do not delete anything from this table
insert into test_list_master values(1, 'Tablet', 'Dissolution');
insert into test_list_master values(2, 'Tablet', 'Disintegration');
insert into test_list_master values(3, 'Tablet', 'Water Content');
insert into test_list_master values(4, 'Tablet', 'Hardness');
insert into test_list_master values(5, 'Hard Gelatin Capsule', 'Brittleness');
insert into test_list_master values(6, 'Hard Gelatin Capsule', 'Dissolution');
insert into test_list_master values(7, 'Hard Gelatin Capsule', 'Disintegration');
insert into test_list_master values(8, 'Hard Gelatin Capsule', 'Water Content');
insert into test_list_master values(9, 'Hard Gelatin Capsule', 'Level of Microbial Contaimination');
insert into test_list_master values(10, 'Soft Gelatin Capsule', 'Dissolution');
insert into test_list_master values(11, 'Soft Gelatin Capsule', 'Disintegration');
insert into test_list_master values(12, 'Soft Gelatin Capsule', 'Level of Microbial Contaimination');
insert into test_list_master values(13, 'Soft Gelatin Capsule', 'PH');
insert into test_list_master values(14, 'Soft Gelatin Capsule', 'Leakage and Pellicle Formation');
--------------------------------------------
select * from test_table_2;
truncate test_table_2;
--------------------------------------------
select * from testtable3;
truncate testtable3;
--------------------------------------------
select * from date_table;
truncate date_table;
--------------------------------------------
select * from sample_id;
alter table sample_id add column date date;
alter table sample_id add column status varchar(45) default null;
truncate sample_id;
--------------------------------------------
select * from schedule_one;
truncate schedule_one;
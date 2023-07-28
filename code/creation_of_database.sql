create database permisions;

create table Employee(email varchar(30) not null,Name varchar(20) not null,Surname varchar(20) not null,NormalDaysOff int not null,ParentialDaysOff int not null,DiseaseDaysOff int not null,primary key(email));

create table Request(RequestId int not null auto_increment,email varchar(30) not null,category varchar(15) not null,RequestedDaysOff int not null,accepted boolean,primary key(RequestId),constraint CHECK_CATEGORY check (category  in  ('NormalDaysOff','ParentialDaysOff','DiseaseDaysOff')));

create table Decision(DecisionId int not null auto_increment,description
varchar(200) not null,viewed boolean not null,reciever varchar(30) not null,primary key(DecisionId));

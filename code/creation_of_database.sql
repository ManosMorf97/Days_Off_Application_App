create database permisions;

create table employee(email varchar(30) not null,Name varchar(20) not null,Surname varchar(20) not null,NormalDaysOff int not null,ParentialDaysOff int n
ot null,DiseaseDaysOff int not null,primary key(email));

create table Request(RequestId int not null auto_increment,email varchar(30) not null,category varchar(15) not null,RequestedDaysOff int not null,accepted boolean,primary key(RequestId),constraint CHECK_CATEGORY check (category in('Normal','Parential','Disease')));

create table Decision(DecisionId int not null auto_increment,description
varchar(200) not null,viewed boolean not null,reciever varchar(30) not null,primary key(DecisionId));

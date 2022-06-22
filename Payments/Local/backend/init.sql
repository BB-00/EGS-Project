-- create database if not exists payments_db;

use payments_db;

create table Wallets(walletID INT NOT NULL AUTO_INCREMENT, username VARCHAR(50) NOT NULL, balance DECIMAL(10,2) NOT NULL, CONSTRAINT wallets_pm PRIMARY KEY(walletID));

alter table Wallets auto_increment=0;

create table Transactions(transactionID INT NOT NULL AUTO_INCREMENT, amount DECIMAL(10,2) NOT NULL, methodID INT NOT NULL, date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, walletID INT NOT NULL, CONSTRAINT transactions_pm PRIMARY KEY(transactionID));

alter table Transactions auto_increment=0;

alter table Transactions add constraint transactions_fk_walletID foreign key (walletID) references Wallets(walletID);

create trigger update_balance after insert on Transactions for each row update Wallets set Wallets.balance = Wallets.balance+new.amount where Wallets.walletID = new.walletID;
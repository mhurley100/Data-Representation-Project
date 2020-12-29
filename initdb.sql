USE DATAREPRESENTATION;


create table shares(
    -> id INT NOT NULL AUTO_INCREMENT,
    -> symbol VARCHAR(30),
    -> name VARCHAR(250),
    -> price INTEGER,
    -> PRIMARY KEY (id)
    -> );

  
create table buyer(
    -> buyerid INT NOT NULL AUTO_INCREMENT,
    -> region VARCHAR(80),
    -> PRIMARY KEY (buyerid),
    -> FOREIGN KEY (buyerid) REFERENCES shares(id)
    -> );

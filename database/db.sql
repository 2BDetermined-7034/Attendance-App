--CREATE TABLE time (   ID INTEGER ,   date TEXT NOT NULL,    time_in TEXT NOT NULL,    time_out TEXT  );

--CREATE TABLE student (   ID INTEGER PRIMARY KEY,   name TEXT NOT NULL,    year INTEGER NOT NULL,    subteam TEXT);


--INSERT INTO student (ID, name, year, subteam)
--VALUES (1, 'Sonan', 2026, 'software');
--VALUES (2, 'alex', 2026, 'software');

--INSERT INTO time (ID, date, time_in, time_out)
--VALUES (1, CURRENT_DATE, CURRENT_TIME, NULL);

select * from student;

select * from time;
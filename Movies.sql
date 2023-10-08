CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL CHECK(length(name) > 0), birth_day DATE);

INSERT INTO people (name, birth_day) VALUES ('Тим Роббинс', '12-02-1975'),
                                            ('Морган Фриман', '13-02-1955'),
                                            ('Том Хэнкс', '21-07-1960'),
                                            ('Дэвид Морс', '22-05-1945'),
                                            ('Майкелти Уильямсон', '24-03-1988')
                                            ('Анн Ле Ни', '15-03-1989');


CREATE TABLE movie (id SERIAL PRIMARY KEY, title VARCHAR(50) NOT NULL,tagline VARCHAR(50), summary TEXT, release_year INT);

INSERT INTO movie (title, tagline, summary, release_year) VALUES(
'The Shawshank Redemption',
'Страх - это кандалы. Надежда - это свобода',
'В основу культовой драмы легла повесть Стивена Кинга «Рита Хейуорт из Шоушенка».',
1994
),
(
'The Green Mile',
'Пол Эджкомб не верил в чудеса. Пока не столкнулся с одним из них',
'Картина снята по одноименному роману Стивена Кинга.',
1999
),
(
'Forrest Gump',
'Мир уже никогда не будет прежним, после того как вы увидите его глазами Форреста Гампа',
'Картина снята по мотивам одноименного романа Уинстона Грума.',
1999
),
(
'The Intouchables',
'Sometimes you have to reach into someone elses world to find out whats missing in your own',
'Филипп очень богатый человек, но в результате несчастного случая его парализовало, и он прикован к инвалидному креслу. Он потерял всякий интерес к жизни, и нуждается в постоянном присмотре.',
2011
);


CREATE TABLE genre (id SERIAL PRIMARY KEY, name VARCHAR(50), movie_id INTEGER REFERENCES movie(id));

INSERT INTO genre(name, movie_id) VALUES ('Drama', 1),
                                         ('Drama', 2),
                                         ('Drama', 3),
                                         ('Drama', 4),
                                         ('Detective', 2),
                                         ('Criminal', 1),
                                         ('Criminal', 2),
                                         ('Fantasy', 2),
                                         ('Comedy', 4),
                                         ('Bio', 4);


CREATE TABLE movie_people (movie_id INTEGER REFERENCES movie(id), people_id INTEGER REFERENCES people(id));

INSERT INTO movie_people VALUES(1,1),
                               (1,2),
                               (2,3),
                               (2,4),
                               (3,3),
                               (3,5),
                               (4,6);

SELECT p.name, m.title FROM people p JOIN movie_people ON p.id = movie_people.people_id JOIN movie m ON movie_people.movie_id = m.id;
SELECT m.title, g.name FROM movie m JOIN genre g ON m.id = g.movie_id;
-- heroku pg:psql < initial_data.sql

-- Countries
INSERT INTO termometer (id, name, lake_position) VALUES (1, 'TOPRIGHT', '10;10');
INSERT INTO termometer (id, name, lake_position) VALUES (2, 'BOTRIGHT', '0;10');
INSERT INTO termometer (id, name, lake_position) VALUES (3, 'TOPLEFT', '10;0');
INSERT INTO termometer (id, name, lake_position) VALUES (4, 'BOTLEFT', '0;0');

-- Authors
INSERT INTO measure (id, termometer_id, temperature) VALUES (1, 1, 32.0);
--INSERT INTO author (id, country_id, name) VALUES (2, 1, 'Mark Twain');
--INSERT INTO author (id, country_id, name) VALUES (3, 4, 'Arthur Conan Doyle');
--INSERT INTO author (id, country_id, name) VALUES (4, 3, 'Jorge Luis Borges');
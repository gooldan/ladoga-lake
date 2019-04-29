drop table if exists termometer;
create table termometer (
  id serial PRIMARY KEY,
  name text not null,
  lake_position text not null
);

drop table if exists measure;
create table measure (
  id serial PRIMARY KEY,
  termometer_id integer REFERENCES termometer (id),
  temperature FLOAT not null
);


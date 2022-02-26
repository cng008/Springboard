-- from the terminal run:
-- psql < adopts.sql
-- psql adopts

DROP DATABASE IF EXISTS adopts;
CREATE DATABASE adopts;
\c adopts;

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT DEFAULT 'https://media.istockphoto.com/vectors/continuous-line-dog-minimalistic-hand-drawing-vector-isolated-vector-id909324004?k=20&m=909324004&s=612x612&w=0&h=8NXfBg_oKfkJ1Rva6G_2PWYvK5RHP2BlSSOR6_7GvQ8=',
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (name, species, photo_url, age, notes, available)
VALUES
  ('Doug', 'dog', 'https://images.pexels.com/photos/97082/weimaraner-puppy-dog-snout-97082.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 1, 'Lovingly playful.', 't'),
  ('Gretta', 'dog', 'https://images.pexels.com/photos/10660184/pexels-photo-10660184.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', 9, 'Gruff but tough', 't'),
  ('Pizza', 'cat', 'https://images.pexels.com/photos/156934/pexels-photo-156934.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', null, 'Found her in an alley eating some pizza, super sweet', 't'),
  ('Mr. Meaty', 'cat', 'https://images.pexels.com/photos/991831/pexels-photo-991831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', null, 'Loves to eat mice, but probably should stop', 't'),
  ('Franklin', 'turtle', null, null, 'Adopted <3', 'f');


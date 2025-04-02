CREATE DATABASE ancestral_archives;
CREATE USER postgres WITH ENCRYPTED PASSWORD 'admin_access989';
GRANT ALL PRIVILEGES ON DATABASE ancestral_archives TO postgres;

CREATE TABLE IF NOT EXISTS person (
	person_id SERIAL PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	age INT,
	birth_date DATE,
	country_origin TEXT,
	state_origin TEXT,
	city_origin TEXT,
	country_current TEXT,
	state_current TEXT,
	city_current TEXT
);

CREATE TABLE IF NOT EXISTS bio (
	bio_id SERIAL PRIMARY KEY,
	bio TEXT,
	person_id INT,
	CONSTRAINT fk_person
		FOREIGN KEY(person_id)
		REFERENCES person(person_id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS story (
	story_id SERIAL PRIMARY KEY,
	story_name TEXT,
	story_text TEXT,
	person_id INT,
	CONSTRAINT fk_person
		FOREIGN KEY(person_id)
		REFERENCES person(person_id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS country (
	country_id SERIAL PRIMARY KEY,
	country_name TEXT
);

CREATE TABLE IF NOT EXISTS state (
	state_id SERIAL PRIMARY KEY,
	state_name TEXT,
	country_id INT,
	CONSTRAINT fk_country
		FOREIGN KEY(country_id)
		REFERENCES country(country_id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS city (
	city_id SERIAL PRIMARY KEY,
	city_name TEXT,
	country_id INT,
	state_id INT,
	CONSTRAINT fk_country
		FOREIGN KEY(country_id)
		REFERENCES country(country_id)
		ON DELETE CASCADE,
	CONSTRAINT fk_state
		FOREIGN KEY(state_id)
		REFERENCES state(state_id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS religion (
	religion_id SERIAL PRIMARY KEY,
	religion_name TEXT
);

CREATE TABLE IF NOT EXISTS race (
	race_id SERIAL PRIMARY KEY,
	race_name TEXT
);

CREATE TABLE IF NOT EXISTS ethnicity (
	ethnicity_id SERIAL PRIMARY KEY,
	ethnicity_name TEXT
);

CREATE TABLE IF NOT EXISTS gender (
	gender_id SERIAL PRIMARY KEY,
	gender_name TEXT
);



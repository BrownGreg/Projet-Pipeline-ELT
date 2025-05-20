-- Création des tables dimensionnelles

CREATE TABLE dim_make (
    make_id SERIAL PRIMARY KEY,
    make_name TEXT UNIQUE NOT NULL
);

CREATE TABLE dim_model (
    model_id SERIAL PRIMARY KEY,
    model_name TEXT UNIQUE NOT NULL,
    make_id INT NOT NULL,
    FOREIGN KEY (make_id) REFERENCES dim_make(make_id)
);

CREATE TABLE dim_transmission (
    transmission_id SERIAL PRIMARY KEY,
    transmission_type TEXT UNIQUE NOT NULL
);

CREATE TABLE dim_fuel (
    fuel_id SERIAL PRIMARY KEY,
    fuel_type TEXT UNIQUE NOT NULL
);

-- Création de la table de faits

CREATE TABLE fact_car_sales (
    sale_id SERIAL PRIMARY KEY,
    make_id INT NOT NULL,
    model_id INT NOT NULL,
    transmission_id INT NOT NULL,
    fuel_id INT NOT NULL,
    year INT NOT NULL,
    price NUMERIC,
    mileage INT,
    tax NUMERIC,
    mpg NUMERIC,
    engine_size NUMERIC,
    FOREIGN KEY (make_id) REFERENCES dim_make(make_id),
    FOREIGN KEY (model_id) REFERENCES dim_model(model_id),
    FOREIGN KEY (transmission_id) REFERENCES dim_transmission(transmission_id),
    FOREIGN KEY (fuel_id) REFERENCES dim_fuel(fuel_id)
);

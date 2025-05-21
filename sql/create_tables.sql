CREATE TABLE IF NOT EXISTS dim_make (
  make_id SERIAL PRIMARY KEY,
  make_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS dim_model (
  model_id SERIAL PRIMARY KEY,
  model_name TEXT,
  make_id INT REFERENCES dim_make(make_id)
);

CREATE TABLE IF NOT EXISTS dim_transmission (
  transmission_id SERIAL PRIMARY KEY,
  transmission_type TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS dim_fuel (
  fuel_id SERIAL PRIMARY KEY,
  fuel_type TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS fact_car_sales (
  sale_id SERIAL PRIMARY KEY,
  make_id INT REFERENCES dim_make(make_id),
  model_id INT REFERENCES dim_model(model_id),
  transmission_id INT REFERENCES dim_transmission(transmission_id),
  fuel_id INT REFERENCES dim_fuel(fuel_id),
  year INT,
  price NUMERIC,
  mileage INT,
  tax NUMERIC,
  mpg NUMERIC,
  engine_size NUMERIC
);

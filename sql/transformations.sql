-- Nettoyage et typage intermédiaire
DROP TABLE IF EXISTS cars_cleaned;
CREATE TABLE cars_cleaned AS
SELECT 
    TRIM(model) AS model,
    year::INTEGER AS year,
    price::NUMERIC AS price,
    TRIM(transmission) AS transmission,
    mileage::INTEGER AS mileage,
    TRIM(fuelType) AS fuel_type,
    tax::NUMERIC AS tax,
    mpg::NUMERIC AS mpg,
    engineSize::NUMERIC AS engine_size,
    TRIM(Make) AS make
FROM cars_raw
WHERE model IS NOT NULL AND year IS NOT NULL AND price IS NOT NULL;

-- Table dimension marque
DROP TABLE IF EXISTS dim_make;
CREATE TABLE dim_make AS
SELECT DISTINCT make AS make_name
FROM cars_cleaned;
ALTER TABLE dim_make ADD COLUMN make_id SERIAL PRIMARY KEY;

-- Table dimension modèle
DROP TABLE IF EXISTS dim_model;
CREATE TABLE dim_model AS
SELECT DISTINCT model AS model_name, make AS make_name
FROM cars_cleaned;
ALTER TABLE dim_model ADD COLUMN model_id SERIAL PRIMARY KEY;

-- Table dimension transmission
DROP TABLE IF EXISTS dim_transmission;
CREATE TABLE dim_transmission AS
SELECT DISTINCT transmission AS transmission_type
FROM cars_cleaned;
ALTER TABLE dim_transmission ADD COLUMN transmission_id SERIAL PRIMARY KEY;

-- Table dimension carburant
DROP TABLE IF EXISTS dim_fuel;
CREATE TABLE dim_fuel AS
SELECT DISTINCT fuel_type
FROM cars_cleaned;
ALTER TABLE dim_fuel ADD COLUMN fuel_id SERIAL PRIMARY KEY;

-- Table dimension année
DROP TABLE IF EXISTS dim_year;
CREATE TABLE dim_year AS
SELECT DISTINCT year
FROM cars_cleaned;
ALTER TABLE dim_year ADD COLUMN year_id SERIAL PRIMARY KEY;

-- Table de faits
DROP TABLE IF EXISTS fact_car_sales;
CREATE TABLE fact_car_sales AS
SELECT 
    c.price,
    c.mileage,
    c.tax,
    c.mpg,
    c.engine_size,
    m.model_id,
    mk.make_id,
    t.transmission_id,
    f.fuel_id,
    y.year_id
FROM cars_cleaned c
JOIN dim_model m ON c.model = m.model_name AND c.make = m.make_name
JOIN dim_make mk ON c.make = mk.make_name
JOIN dim_transmission t ON c.transmission = t.transmission_type
JOIN dim_fuel f ON c.fuel_type = f.fuel_type
JOIN dim_year y ON c.year = y.year;

-- Indexation pour performance
CREATE INDEX ON fact_car_sales(model_id);
CREATE INDEX ON fact_car_sales(make_id);
CREATE INDEX ON fact_car_sales(transmission_id);
CREATE INDEX ON fact_car_sales(fuel_id);
CREATE INDEX ON fact_car_sales(year_id);

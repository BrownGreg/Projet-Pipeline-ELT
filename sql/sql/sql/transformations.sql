-- Insérer les marques distinctes dans dim_make
INSERT INTO dim_make (make_name)
SELECT DISTINCT make
FROM raw_cars
WHERE make IS NOT NULL;

-- Insérer les modèles distincts dans dim_model
INSERT INTO dim_model (model_name, make_id)
SELECT DISTINCT bd.model, dm.make_id
FROM raw_cars bd
JOIN dim_make dm ON bd.make = dm.make_name
WHERE bd.model IS NOT NULL;

-- Insérer les types de transmission distincts dans dim_transmission
INSERT INTO dim_transmission (transmission_type)
SELECT DISTINCT transmission
FROM raw_cars
WHERE transmission IS NOT NULL;

-- Insérer les types de carburant distincts dans dim_fuel
INSERT INTO dim_fuel (fuel_type)
SELECT DISTINCT fuelType
FROM raw_cars
WHERE fuelType IS NOT NULL;

-- Insérer les données dans la table de faits fact_car_sales
INSERT INTO fact_car_sales (
    make_id, model_id, transmission_id, fuel_id, year, price, mileage, tax, mpg, engine_size
)
SELECT
    dm.make_id,
    dmod.model_id,
    dt.transmission_id,
    df.fuel_id,
    bd.year,
    bd.price,
    bd.mileage,
    bd.tax,
    bd.mpg,
    bd.engineSize
FROM raw_cars bd
JOIN dim_make dm ON bd.make = dm.make_name
JOIN dim_model dmod ON bd.model = dmod.model_name AND dmod.make_id = dm.make_id
JOIN dim_transmission dt ON bd.transmission = dt.transmission_type
JOIN dim_fuel df ON bd.fuelType = df.fuel_type;

import pandas as pd

def test_csv_columns():
    df = pd.read_csv("data/raw/cars_dataset.csv")
    df.columns = df.columns.str.strip().str.lower()
    expected_cols = {
        "model", "year", "price", "transmission", "mileage",
        "fueltype", "tax", "mpg", "enginesize", "make"
    }
    assert expected_cols.issubset(set(df.columns)), "❌ Colonnes manquantes dans le CSV"

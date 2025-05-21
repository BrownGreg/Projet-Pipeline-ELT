import os
import pandas as pd

def test_csv_columns():
    main_path = "data/raw/cars_dataset.csv"
    sample_path = "data/raw/cars_dataset_sample.csv"
    if os.path.exists(main_path):
        path = main_path
    elif os.path.exists(sample_path):
        path = sample_path
    else:
        assert False, f"❌ Aucun fichier CSV trouvé : {main_path} ni {sample_path}"
    df = pd.read_csv(path)
    expected_columns = [
        "model", "year", "price", "transmission", "mileage",
        "fuelType", "tax", "mpg", "engineSize", "Make"
    ]
    assert list(df.columns) == expected_columns, f"❌ Colonnes inattendues : {df.columns.tolist()}"

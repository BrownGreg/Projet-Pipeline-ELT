import os
import pandas as pd

def test_csv_exists_and_loadable():
    path = "data/raw/cars_dataset.csv"
    assert os.path.exists(path), f"❌ Fichier non trouvé : {path}"

    df = pd.read_csv(path)
    assert not df.empty, "❌ Le fichier CSV est vide"

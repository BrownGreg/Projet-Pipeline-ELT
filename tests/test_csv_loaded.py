import os
import pandas as pd

def test_csv_exists_and_loadable():
    main_path = "data/raw/cars_dataset.csv"
    sample_path = "data/raw/cars_dataset_sample.csv"
    if os.path.exists(main_path):
        path = main_path
    elif os.path.exists(sample_path):
        path = sample_path
    else:
        assert False, f"❌ Aucun fichier CSV trouvé : {main_path} ni {sample_path}"
    df = pd.read_csv(path)
    assert not df.empty, f"❌ Le fichier {path} est vide."

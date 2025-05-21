# src/model/DataPreprocessingMS.py
import pandas as pd

class DataPreprocessingMS:
    def __init__(self):
        pass

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        # Simplemente devolvemos una copia: 
        # el reindex y fill_value=0 ocurre en el controlador
        return df.copy()

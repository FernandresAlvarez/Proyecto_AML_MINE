#RandomForest

import numpy as np
import pandas as pd

class DataPreprocessingMLPRegressor:

    def __init__(self):
        print("DataPreprocessingMLPRegressor.__init__ ->")
        #self.target_feature = "labels"

    def transform(self, df):
        print("DataPreprocessingMLPRegressor.transform ->")
        X_test = df
        return X_test

    def get_columns(self):
        print("DataPreprocessingMLPRegressor.get_columns ->")
        return {'ranking', 'temp_ranking', 'previous_ranking', 'city', 'country',
       'state', 'current_employees', 'employee_growth', 'total_funding',
       'Industry', 'Points', 'valuation', 'best_score',
       'score_category', 'match_score'}
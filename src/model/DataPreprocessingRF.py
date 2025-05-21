#RandomForest

import numpy as np
import pandas as pd

class DataPreprocessingRF:

    def __init__(self):
        print("DataPreprocessingRF.__init__ ->")
        #self.target_feature = "labels"

    def transform(self, df):
        print("DataPreprocessingRF.transform ->")
        X_test = df
        return X_test

    def get_categories(self):
        print("DataPreprocessingRF.get_categories ->")
        return ["Closed", "Acquired"]

    def get_cat_name(self, index):
        print("DataPreprocessingRF.get_cat_name ->")
        if index < 0 or index > 1:
            return ""
        return self.get_categories()[index]


    def get_columns(self):
        print("DataPreprocessingRF.get_columns ->")
        return {'is_enterprise', 'has_roundA', 'is_ecommerce', 'is_advertising',
       'is_CA', 'is_MA', 'has_roundD', 'is_mobile', 'is_top500', 'is_TX',
       'avg_participants', 'milestones', 'is_software', 'is_web',
       'category_code', 'is_consulting', 'is_otherstate', 'is_gamesvideo',
       'relationships', 'funding_total_usd', 'has_angel', 'has_roundB',
       'has_VC', 'is_biotech', 'has_roundC', 'is_othercategory',
       'funding_rounds', 'is_NY', 'labels'}
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from math import sin, cos, sqrt, atan2, radians


class Pre_processing:
    def __init__(self) -> None:
        pass

    def diff_date(self,
                  df,
                  col1,
                  col2):
        a = 0
        for i in range(df.shape[0]):
            if(df[col1][i] == df[col2][i]):
                a = 1
                if(a == 0):
                    x = df(col1)[i]
                    y = df(col2)[i]
        return print(f"Date is different. Pickup Date = {x} and Dropoff Date is {y}")
    
    def calculate_iqr_limits(self, df, column_name):
        iqr = column_name.quantile(0.75) - column_name.quantile(0.25)
        upper_limit = column_name.quantile(0.75) + 1.5 * iqr
        lower_limit = column_name.quantile(0.25) - 1.5 * iqr
        return upper_limit, lower_limit
    
    def distance_func(self, lat1, lon1, lat2, lon2):
        lat1_rad = radians(lat1)
        lon1_rad = radians(lon1)
        lat2_rad = radians(lat2)
        lon2_rad = radians(lon2)   
        radius = 6371.0    
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad    
        a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = radius * c    
        return distance
    
    def calculate_distances(self, df, lat1_col, lon1_col, lat2_col, lon2_col):
        distances = []
        for i in range(df.shape[0]):
            lat1 = df[lat1_col].iloc[i]
            lon1 = df[lon1_col].iloc[i]
            lat2 = df[lat2_col].iloc[i]
            lon2 = df[lon2_col].iloc[i]    
            if pd.notnull(lat1) and pd.notnull(lon1) and pd.notnull(lat2) and pd.notnull(lon2):
                distance = self.distance_func(lat1, lon1, lat2, lon2)
                distances.append(distance)
            else:
                distances.append(np.nan)
        distances_series = pd.Series(distances, name='distance')
        df_reset = df.reset_index(drop=True)
        distances_reset = distances_series.reset_index(drop=True)
        concatenated_df = pd.concat([df_reset, distances_reset], axis=1)
        return concatenated_df
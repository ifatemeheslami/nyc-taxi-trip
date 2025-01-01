import pandas as pd
import numpy as np
from geopy.distance import geodesic
from datetime import datetime, timedelta


class Data_loader:
    def __init__(self) -> None:
        pass

    #  Loading Data:
    def loading(self, data_path):
        df = pd.read_csv(data_path)
        return df
    
    def split_datetime_columns(self, df):
        pickup_date = []
        pickup_time = []
        dropoff_date = []
        dropoff_time = []
        for i in range(df.shape[0]):
            a = df["pickup_datetime"][i].split(" ")
            b = df["dropoff_datetime"][i].split(" ")
            pickup_date.append(a[0])
            pickup_time.append(a[1])
            dropoff_date.append(b[0])
            dropoff_time.append(b[1])
        pickup_date = pd.Series(pickup_date, name="pickup_date")
        pickup_time = pd.Series(pickup_time, name="pickup_time")
        dropoff_date = pd.Series(dropoff_date, name="dropoff_date")
        dropoff_time = pd.Series(dropoff_time, name="dropoff_time")
        modified_dataframe = pd.concat([df, pickup_date, pickup_time, dropoff_date, dropoff_time], axis=1)
        return modified_dataframe
    
    def convert_columns_to_datetime(self, modified_dataframe,cols):
        for col in cols:
            modified_dataframe[col] = pd.to_datetime(modified_dataframe[col])
        return modified_dataframe

    def column_rename(self, df_split):
        new_column = {0: "pickup_date", 1: "pickup_time", 2: "dropoff_date", 3: "dropoff_time"}
        df_split.rename(columns = new_column, inplace = True)
        return df_split

    def time_columns(self, df_new, datetime_column):
        df_new["year"] = df_new[datetime_column].dt.year
        df_new["month"] = df_new[datetime_column].dt.month
        df_new["day"] = df_new[datetime_column].dt.day
        df_new["hour"] = df_new[datetime_column].dt.hour
        df_new["minute"] = df_new[datetime_column].dt.minute
        df_new["second"] = df_new[datetime_column].dt.second
        df_new = df_new.reset_index(drop=True)
        return df_new
    
    def clean_passenger_count(self, df):
        for i in range(df.shape[0]):
            if df.at[i, "passenger_count"] in [0, 7, 8, 9]:
                df.at[i, "passenger_count"] = np.nan
        return df


class Converting():

    def __init__(self) -> None:
        pass

    def to_datetime(self, df_datetime, datetime_cols):
        for col in datetime_cols:
            df_datetime[col] = pd.to_datetime(df_datetime[col])
        return df_datetime

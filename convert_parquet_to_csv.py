
import pandas as pd
import pathlib
import os

# INSERT THE NAME OF THE FOLDER YOU WOULD LIKE TO CHANGE ALL .parquet FILES TO .csv
folder_path = 'C:/Desktop/folder'


# DETERMINES IF THE FILE IS A .parquet FILE OR NOT
def is_parquet(filepath):
    file_extension = pathlib.Path(filepath).suffix
    file_extension = file_extension.replace('.', '').lower()
    file_extension = file_extension.strip()
    pqt = 'parquet'

    if file_extension == pqt:
        return True
    else:
        return False


# CONVERT .parquet TO .csv
def conv_parquet_to_csv(filepath):
    filepath_name = pd.read_parquet(filepath)
    filepath_new = filepath.replace('.parquet', '.csv')
    filepath_name.to_csv(filepath_new)


# LOOP THROUGH SPECIFIED FOLDER AND CONVERT ALL PARQUET FILES TO CSV
def conv_all_parquet_in_folder_to_csv(folder_filepath):
    all_files = os.listdir(folder_filepath)
    for file in all_files:
        filepath = folder_filepath + '/' + file
        if is_parquet(file) is True:
            conv_parquet_to_csv(filepath)


conv_all_parquet_in_folder_to_csv(folder_path)


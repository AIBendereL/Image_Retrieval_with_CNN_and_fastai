# AUTOGENERATED! DO NOT EDIT! File to edit: ../log.ipynb.

# %% auto 0
__all__ = ['log_excel', 'r_precision_to_dataframe', 'dataframes_to_excel']

# %% ../log.ipynb 1
from pathlib import Path

import pandas as pd
import torch

# %% ../log.ipynb 4
def log_excel(dts_li, model_li, r_precision_li, r_li):

    name = [ [dts.name, model.name] for dts in dts_li for model in model_li]
    df_name = pd.DataFrame(name, columns= ["dts", "mdl"])

    r_precision_li = torch.round(r_precision_li, decimals= 4)
    df_r_precision = pd.DataFrame(r_precision_li, columns= r_li)
    
    output = pd.concat([df_name, df_r_precision], axis= 1)

    log_folder = Path("log/")
    log_name = "log.xlsx"
    log_path = log_folder/log_name
    output.to_excel(log_path)

    return output


# non-original
def r_precision_to_dataframe(dts, model, r_precision, r_li, idx= 0):

    name = [ [dts.name, model.name]]
    df_name = pd.DataFrame(name, columns= ["dts", "model"], index= [idx])

    r_precision = torch.round(r_precision, decimals= 4).unsqueeze(0)
    df_r_precision = pd.DataFrame(r_precision, columns= r_li, index= [idx])

    return pd.concat([df_name, df_r_precision], axis= 1)

# non-original
def dataframes_to_excel(df_li):

    output = pd.concat(df_li, axis= 0)

    log_folder = Path("log/")
    log_name = "dataframes_to_excel.xlsx"
    log_path = log_folder/log_name
    output.to_excel(log_path)

    return output
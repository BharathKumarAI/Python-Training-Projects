# Import required libraries
from ast import literal_eval
import os
import logging
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Packages for reading configuration files
import hydra
from hydra.core.config_store import ConfigStore
from hydra.utils import to_absolute_path as abspath
from omegaconf import DictConfig

# Association Rule Learning (ARL)
import apyori as ap


import warnings

warnings.filterwarnings("ignore")


@hydra.main(config_path="../config", config_name="main")
def log_file_obj(config: DictConfig):
    """Function to log the file object"""
    log_folder_path = abspath(config.logs.path)
    # filename with the date and time
    log_file_name = (
        config.logs.fileFormat
        + datetime.datetime.now().strftime("%Y%M%d%H%m%S")
        + ".log"
    )

    log_file_path = os.path.join(log_folder_path, log_file_name)

    log_file = open(log_file_path, "w")

    return log_file


@hydra.main(config_path="../config", config_name="main")
def read_data(config: DictConfig):
    """Function to read the data"""
    print(config)
    raw_path = abspath(config.data.raw.path)
    print(f"Read data using {raw_path}")

    # hydra configuration to get current working directory: ${hydra:runtime.cwd}/../data/raw/
    # Read the data
    if config.data.raw.format == "csv":
        usr_sep = config.data.raw.separator
        if not usr_sep:
            usr_sep = ","

        header = literal_eval(config.data.raw.header)
        if header:
            df = pd.read_csv(raw_path, header=0)
        else:
            if config.data.raw.skip_rows:
                df = pd.read_csv(
                    raw_path,
                    skiprows=config.data.raw.skip_rows,
                    header=header,
                )
            else:
                df = pd.read_csv(raw_path)
    else:
        raise Exception("Currently only csv files are supported")

    # Print the first 5 rows
    print(df.head())

    return df


def convert_as_transactions(df):
    """Function to convert the data into transactions"""

    transactions = []

    for i in range(0, df.shape[0]):
        transactions.append(
            [str(df.values[i, j]) for j in range(0, df.shape[1])]
        )

    return transactions

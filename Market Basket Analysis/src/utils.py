# Import required libraries
from ast import literal_eval
import os
import yaml
import tqdm
import logging
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Association Rule Learning (ARL)
import apyori as ap


import warnings

warnings.filterwarnings("ignore")


logger = logging.getLogger("MarketBasketAnalysis.utils")


def config_file_reader(config_file):
    """Function to read the configuration yaml file"""
    logger.info("Reading configuration file from: {}".format(config_file))
    with open(config_file, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    logger.info("Successfully read the configuration file: " + str(config))
    return config


def log_file_obj(config):
    """Function to log the file object"""
    logger.info(f"Log file: {config['logs']['path']}")
    log_folder_path = config["logs"]["path"]
    # filename with the date and time
    log_file_name = (
        config["logs"]["fileFormat"]
        + datetime.datetime.now().strftime("%Y%M%d%H%m%S")
        + ".log"
    )

    log_file_path = os.path.join(log_folder_path, log_file_name)

    log_file = open(log_file_path, "w")

    return log_file


def read_data(config) -> pd.DataFrame:
    """Function to read the data"""
    raw_path = config["data"]["raw"]["path"]
    logger.info(f"Reading data from: {raw_path}")

    # Read the data
    if config["data"]["raw"]["format"] == "csv":
        usr_sep = config["data"]["raw"]["separator"]
        if not usr_sep:
            usr_sep = ","

        header = literal_eval(config["data"]["raw"]["header"])
        if header:
            df = pd.read_csv(raw_path, header=0)
        else:
            if config["data"]["raw"]["skip_rows"]:
                df = pd.read_csv(
                    raw_path,
                    skiprows=config["data"]["raw"]["skip_rows"],
                    header=header,
                )
            else:
                df = pd.read_csv(raw_path)
        logger.info("Reading data has been finished sucessfully")
        logger.info(df.head())
        return df
    else:
        raise Exception("Currently only csv files are supported")


def convert_as_transactions(df):
    """Function to convert the data into transactions"""
    logger.info("Converting data into transactions has been started")
    print(df.head())
    transactions = []

    for i in tqdm.tqdm(range(0, df.shape[0])):
        # Apiri requires a list of lists of items in each transaction with string values
        transactions.append(
            [str(df.values[i, j]) for j in range(0, df.shape[1])]
        )
    logger.info("Converting data into transactions has been finished")
    return transactions


def inspect(results):
    """Function to inspect the results"""
    logger.info("Inspecting the results has been started")
    lhs = [tuple(result[2][0][0]) for result in results]
    rhs = [tuple(result[2][0][1]) for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return lhs, rhs, supports, confidences, lifts

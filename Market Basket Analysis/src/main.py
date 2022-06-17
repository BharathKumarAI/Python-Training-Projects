# Import required libraries
import os
import sys
import logging
import datetime
import numpy as np
import pandas as pd
from ast import literal_eval
import matplotlib.pyplot as plt

# Import utils.py
from utils import *

# Packages for reading configuration files
import hydra
from hydra.core.config_store import ConfigStore
from hydra.utils import to_absolute_path as abspath
from omegaconf import DictConfig

# Association Rule Learning (ARL)
import apyori as ap


import warnings

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    # Read the data
    df = read_data()
    print(df)
    # convert the data into transactions
    transactions = convert_as_transactions(df)

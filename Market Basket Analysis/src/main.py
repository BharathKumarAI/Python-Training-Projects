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
from config import MarketBasketConfig

# Packages for reading configuration files
import hydra
from hydra.core.config_store import ConfigStore
from hydra.utils import to_absolute_path as abspath
from omegaconf import DictConfig

# Association Rule Learning (ARL)
import apyori as ap


import warnings

warnings.filterwarnings("ignore")

cs = ConfigStore.instance()
cs.store(name="marketbasket_config", node=MarketBasketConfig)

log_file = log_file_obj()

sys.stdout = log_file

df = read_data()
transactions = convert_as_transactions(df)

sys.stdout = sys.stdout

log_file.close()

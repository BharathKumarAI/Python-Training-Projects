# Import required libraries
import logging
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import utils.py
from utils import *

# Association Rule Learning (ARL)
from apyori import apriori


import warnings

warnings.filterwarnings("ignore")

# create logger with 'Market Basket Analysis'
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
    filename=f"Market Basket Analysis/logs/market_basket_analysis_{datetime.datetime.now().strftime('%Y%M%d%H%m%S')}.log",
    filemode="a",
)
logger = logging.getLogger("Market Basket Analysis")


if __name__ == "__main__":
    logger.info("Starting the process")

    # Read the configuration file
    config_file_path = "Market Basket Analysis/main.yaml"
    config = config_file_reader(config_file_path)

    # Read the data
    df = read_data(config)

    # convert the data into transactions
    transactions = convert_as_transactions(df)

    model = config["defaults"]["model"]

    if model == "apriori":
        # Apply Apriori algorithm
        logger.info("Applying Apriori algorithm")

        # recommended formula for min_support is
        # min_support = (number of minimum transactions*frequency of the item in the transaction set)/total number of transactions
        # choosing of minimum lift of 3 is recommended by the user
        # calling the apriori function to get the association rules
        rules = apriori(
            transactions=transactions,
            min_support=config[model]["min_support"],
            min_confidence=config[model][
                "min_confidence"
            ],  # usually 0.8 is recommended
            min_lift=config[model]["min_lift"],  # 3 is the minimum lift
            min_length=config[model][
                "min_length"
            ],  # minimum number of items we want to include in the rule
            max_length=config[model][
                "max_length"
            ],  # maximum number of items we want to include in the rule
        )

        # finding the best rules where
        # Buying one product A will give product B as free -min_length=2, max_length=2
        # Buying 2 products of A will get B product for free - max_length=3, min_length=3

        # getting the rules and the corresponding support, confidence values
        results = list(rules)

        if len(results) == 0:
            logger.error("No association rules found")
            raise Exception("No association rules found")
        else:
            logger.info("Association rules found")

            # getting the rules and the corresponding support, confidence values as a dataframe
            resultsinDataFrame = pd.DataFrame(
                inspect(results),
                columns=[
                    "Left Hand Side",
                    "Right Hand Side",
                    "Support",
                    "Confidence",
                    "Lift",
                ],
            )

            dataset_name = (
                config["data"]["raw"]["path"].split("/")[-1].split(".")[0]
            )
            # writing the results to a csv file
            resultsinDataFrame.to_csv(
                f"Market Basket Analysis/results/Output_{dataset_name}_{datetime.datetime.now().strftime('%Y%M%d%H%m%S')}.csv",
                index=False,
            )
            # Display the best 10 rules
            logger.info("Displaying the best 10 rules by Lift")
            logger.info(resultsinDataFrame.nlargest(10, "Lift"))

            logger.info("Sucessfully completed the process")

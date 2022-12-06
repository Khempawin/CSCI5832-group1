# from typing import 
import pandas as pd
# Load Data from files
# Load arguments
def load_arguments(filename:str):
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
        headers = lines[0].strip().split("\t")
        records = [l.strip().split("\t") for l in lines[1:]]
    return headers, records

def load_arguments_as_df(filename:str):
    return pd.read_csv(filename, encoding="utf8", sep="\t").set_index("Argument ID")

def load_value_categories(filename:str):
    return pd.read_csv(filename, encoding="utf8", sep="\t").set_index("Argument ID")
# Encode labels to vector space

opposite_pairs = {
    "0": [],
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": [],
    "13": [],
    "14": [],
    "15": [],
    "16": [],
    "17": [],
    "18": [],
    "19": [],
}
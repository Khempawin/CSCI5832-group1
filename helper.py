# from typing import
import pandas as pd
# Load Data from files
# Load arguments


def load_arguments(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
        headers = lines[0].strip().split("\t")
        records = [l.strip().split("\t") for l in lines[1:]]
    return headers, records


def load_arguments_as_df(filename: str):
    return pd.read_csv(filename, encoding="utf8", sep="\t").set_index("Argument ID")


def load_value_categories(filename: str):
    return pd.read_csv(filename, encoding="utf8", sep="\t").set_index("Argument ID")
# Encode labels to vector space

opposite_pairs = {
    "Self-direction: thought": (0, 1),
    "Self-direction: action": (1, 1),
    "Stimulation": (2, 1),
    "Hedonism": (3, 1),
    "Achievement": (4, 1),
    "Power: dominance": (5, 1),
    "Power: resources": (6, 1),
    "Face": (7, 1),
    "Security: personal": (8, 1),
    "Security: societal": (9, 1),
    "Tradition": (0, -1),
    "Conformity: rules": (1, -1),
    "Conformity: interpersonal": (2, -1),
    "Humility": (3, -1),
    "Benevolence: caring": (4, -1),
    "Benevolence: dependability": (5, -1),
    "Universalism: concern": (6, -1),
    "Universalism: nature": (7, -1),
    "Universalism: tolerance": (8, -1),
    "Universalism: objectivity": (9, -1),
}

pair_dict = {
    0: ['Self-direction: thought', 'Tradition'], 
    1: ['Self-direction: action', 'Conformity: rules'], 
    2: ['Stimulation', 'Conformity: interpersonal'], 
    3: ['Hedonism', 'Humility'], 
    4: ['Achievement', 'Benevolence: caring'],
    5: ['Power: dominance', 'Benevolence: dependability'], 
    6: ['Power: resources', 'Universalism: concern'], 
    7: ['Face', 'Universalism: nature'], 
    8: ['Security: personal', 'Universalism: tolerance'], 
    9: ['Security: societal', 'Universalism: objectivity']
    }


def encode_label(inputRow):
    output_vector = [0] * len(pair_dict)
    for k, v in pair_dict.items():
        output_vector[k] = inputRow[v[0]] + inputRow[v[1]] * -1
    return output_vector

def decode_label(embeddedVal, threshold=0.3):
    out = [0] * 20
    for i, v in pair_dict.items():
        if(embeddedVal[i] >= threshold):
            out[i] = 1
        elif(embeddedVal[i] <= (-threshold)):
            out[i + 10] = 1
    return out


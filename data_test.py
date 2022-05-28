
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import pandas as pd
import numpy as np
import json

# load file
f = open("orderbooks_05jul21.json")

# Convert JSON into Dictionary
ob_data = json.load(f)

# Extrac list from json
bitfinix_list = list(ob_data["bitfinex"].keys())
kraken_list = list(ob_data["kraken"].keys())

if __name__ == "__main__":
    print(kraken_list)

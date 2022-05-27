
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

# Opening JSON file
f = open()

#Returns JSON object as a dictionary
orderbooks_data = json.load(f)

orderbooks_data.keys()

bitfinex_ts = list(orderbooks_data['bitfinex'].keys())
kraken_ts = list(orderbooks_data['kraken'].keys())

ob_data = orderbooks_data['bitfinex']
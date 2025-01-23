# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# TEST TRAINING WITH ADANIENT DATASET

import pandas as pd
import os
from sklearn.model_selection import train_test_split

# +

working_dir = os.getcwd()

# Construct the path to the 'data' directory relative to the working directory
folder_path = os.path.join(working_dir, "data")
df = pd.read_csv(os.path.join(folder_path, "updated_ADANIENT.csv"))
df.head()
# -



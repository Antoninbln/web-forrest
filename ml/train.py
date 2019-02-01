"""
The :mod:`ml.train` module implements utilities
to train a model
@param {List < String >} features
@param { String } filepath
@return { Void } Save model
@return { string } file path

- Fit
- Crossvalidation
"""
# Author: Charles Paulas Victor

import pandas as pd

def open_dataset(filepath):
  """
  function open_dataset: 

  Parameters
  ----------
  filepath: string
  File path of the clean dataset

  Return 
  -------
  df_res : pd.DataFrame
  Return a dataframe ready to use for training

  """
  df_res = pd.read_csv(filepath)

  return df_res

# TEST

PATH_TO_FILE = "../data/dataset.csv"

res = open_dataset(PATH_TO_FILE)
print(res)

#print(open_data)


# END TEST
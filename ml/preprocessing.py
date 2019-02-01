import pandas as pd
import os


class Preprocessing:
  """
    Clean data as DataFrame
  """

  def __init__(self, input_data):
    self.input = input_data
    self.data = input_data
    self.output_data = self.clean()
  
  def get_columns(self):
    """
      Get list of columns name

      Return
      ----------------
      Serie<String> : Serie of columns name
    """
    return self.data.columns
  
  def clean(self):
    """
      Remove null / na values in the dataset
      1. Check the proportion of null values in each columns
      2. Remove or not columns depending on null values proportion
      3. Remove rows where there is a null value

      Return
      ----------------
      DataFrame : cleaned dataset (so we can call it inside a chain)
    """
    NULL_LIMIT_PROPORTION = 0.15
    dataset_length = self.data.shape[0]

    # Checking if there is null values in columns
    for column in self.data:
      null_counter = self.data[column].isna().sum()

      # If there is more than 15% of null values
      if (null_counter / dataset_length) > NULL_LIMIT_PROPORTION:
        # Removing column
        self.data = self.data.drop(column, axis=1)

    # Then remove all rows of null values
    cleaned_data = self.data.dropna().reset_index(drop=True)
    self.data = cleaned_data
    return self.data

  def get_data(self):
    """
      Get dataset

      Return
      ----------------
      DataFrame : Dataset
    """
    return self.data

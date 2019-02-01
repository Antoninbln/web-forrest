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

class Train:
  """
  class dedicated for training
  """

  def __init__(self, filepath, features):
    self.filepath = filepath
    self.features = features
    self.df = Train.open_dataset(self.filepath) # TODO : check if "Train." is needed
    self.df_filtered = Train.filter_dataset(self.df, self.features)

  def get_filepath(self):
    return self.filepath

  def get_features(self):
    return self.features

  def get_df_filtered(self):
    return self.df_filtered

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
    Return a dataframe ready to use for filtering

    """
    df_res = pd.read_csv(filepath)
    return df_res

  def filter_dataset(df, features):
    """
    function filter_dataset: 

    Parameters
    ----------
    df: pd.DataFrame
    DataFrame of the clean dataset provided by open_dataset

    features: list
    List of column names provided by the user

    Return 
    -------
    df_res : pd.DataFrame
    Return a dataframe ready to use for training

    """
    df_res = df[features]

    return df_res

# TEST

PATH_TO_FILE = "../data/dataset.csv"
features= ['name', 'category', 'currency']


# Test 1 : ouverture et affichage du dataset d'entrée
#res = open_dataset(PATH_TO_FILE)
#print(res)

# Test 2 : ouverture du DataFrame filtré, affichage du dataset,
# et comparaison de la taille du dataframe

#res = open_dataset(PATH_TO_FILE)
# Print names of column from the data frame
#print(res.columns.tolist())

#print("raw data size : ",res.shape)

#res_filtered = filter_dataset(res, features)
#print("raw data size : ",res_filtered.shape)

# Test 3 : Test 1 et 2 en objet
t = Train(PATH_TO_FILE, features)
print(t.get_df_filtered().shape)




# END TEST

# EXAMPLE
"""
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
"""
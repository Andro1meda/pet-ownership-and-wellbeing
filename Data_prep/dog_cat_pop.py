# import all necessary libraries
import pandas as pd
import numpy as np 
from IPython.display import display

# read in .csv files
cat_pop = pd.read_csv('Cat_pop.csv')
dog_pop = pd.read_csv('dog_pop.csv')

# view top 5 rows for both 
#print(cat_pop.head())
#print(dog_pop.head())

# remove trailing spaces from cat population
cat_pop['District'] = cat_pop['District'].str.strip()

# merge both datasets based on district 
merged_data = pd.merge(cat_pop, dog_pop, on='District')
#print(merged_data.head())

# check for NaN values
nan_check = merged_data.isna()
#print(nan_check)

# convert into data frame
cat_dog_pop = pd.DataFrame(merged_data)

# selecting columns, discarding the rest
cat_dog_pop = cat_dog_pop.drop(['In mil', '% of cat-owning households', 'EstimatedDogPopulation', 'perc_dog_households'], axis = 1)
print(cat_dog_pop)

# turn into csv file
cat_dog_pop.to_csv('cat_dog_pop.csv')
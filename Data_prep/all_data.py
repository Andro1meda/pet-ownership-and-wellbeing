import pandas as pd
import numpy as np 
from IPython.display import display 

# read in data 
data = pd.read_csv('Wellbeing.csv', encoding='cp1252')

# get 5 rows
#print(data.head())

# data types
#print(data.dtypes)


# change anxiety, worthwhile, life satisfaction, happiness into numerical

data[['Anxiety', 'Worthwhile', 'Life Satisfaction', 'Happiness']] = data[['Anxiety', 'Worthwhile', 'Life Satisfaction', 'Happiness']].apply(pd.to_numeric, downcast = 'float', errors='coerce')
#print(data.dtypes)

# select only district, anxiety, worthwhile, life satisfaction and happiness - remove area name
data_new = data.drop('Area Name', axis=1)
#print(data_new.head())

# check for na values
#print(data_new.isna())
data_new = data_new.dropna()

# group by district then get the mean of each 

grouped_data = data.groupby('District').mean()
print(grouped_data)

# convert to dataframe 

well_being_data = pd.DataFrame(grouped_data)

# convert csv

well_being_data.to_csv('well_being.csv')

# read in dog and cat data that you need
dog_cat_pop = pd.read_csv('cat_dog_pop.csv')
wellbeing = pd.read_csv('well_being.csv')

# merge all data together
all_data = pd.merge(dog_cat_pop, wellbeing, on= 'District')
display(all_data.head())

# convert into a data frame 
all_data = pd.DataFrame(all_data)

# remove unnamed column
all_data = all_data.loc[:, ~all_data.columns.str.contains('^Unnamed')]

# convert to csv file
all_data.to_csv('all_data.csv')
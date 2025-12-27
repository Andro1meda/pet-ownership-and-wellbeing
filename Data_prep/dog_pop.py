from IPython.display import display
import pandas as pd
print(pd.__version__)
import numpy as np

# load data
dog_population = pd.read_csv('APHA0375-Dog_Density_Postcode_District.csv')

# print top 5 rows
print(dog_population.head())

# select columns by label
dog_pop_select = dog_population.loc[:,['PostcodeDistrict', 'EstimatedDogPopulation', 'Area Name', 'District']]
print(dog_pop_select.head())

# remove rows with at least one NaN value
dog_pop_select_new = dog_pop_select.dropna()
print(dog_pop_select_new)

# check data types
dog_pop_select_new.dtypes

# remove commas
dog_new = dog_pop_select_new.replace(',','', regex=True) 
print(dog_new)

# remove trailing spaces
dog_new['District'] = dog_new['District'].str.strip()

# convert data type
dog_new['EstimatedDogPopulation'] = pd.to_numeric(dog_new['EstimatedDogPopulation'].astype(float))
print(dog_new.dtypes)

# aggregating results - join the values of all based on district 
area_all_pop = dog_new.groupby('District')['EstimatedDogPopulation'].sum()
print(area_all_pop)


# convert to data frame
area_all = pd.DataFrame(area_all_pop)

# add a new column with percentage of dog-owning households
area_all = area_all.assign(perc_dog_households = [32,35,31,40,38,36,29,32,41,35,34])
#display(area_all)

# add a column of total dog owners per district
area_all = area_all.assign(dog_owners = lambda x: x.EstimatedDogPopulation * (x.perc_dog_households / 100))
display(area_all)

# export data to csv file
area_all.to_csv('dog_pop.csv')






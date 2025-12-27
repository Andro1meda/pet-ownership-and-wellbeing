import pandas as pd
import numpy as np
import pyreadstat

# using pyreadstat to read .sav file
sh_data, meta = pyreadstat.read_sav('SCAS YPMH Dataset.sav')

#print(sh_data)

# convert to csv file
sh_data.to_csv('sh_data.csv')

# select the important data 
sh_data_selected = sh_data.loc[:, ['gender', 'pet_owner', 'num_cat', 'num_dog', 'hads_anxiety', 'hads_depression', 'sbq1_lietime','sbq2_pastyear','sbq3_disclosure',
                                   'sbq4_future','sbq_total']]

#print(sh_data_selected)

# check data types 
print(sh_data_selected.dtypes) 

# remove na values 

sh_data_selected = sh_data_selected.dropna()

# rename columns

sh_data_selected.rename(columns={'sbq1_lietime': 'sbq1_lifetime'}, inplace = True)

# turn into a data frame

sh_data_new = pd.DataFrame(sh_data_selected)

# turn into csv file 
sh_data_new.to_csv('sh_data_all.csv')








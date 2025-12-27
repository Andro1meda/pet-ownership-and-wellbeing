# load in libraries needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read in the file
pop_data = pd.read_csv("all_data.csv")
##--------------------------------------------------
# RQ3: regional levels of cat and dog ownershup associated with well-being

#-------Correlation---------------------
# check for assumptions of normality
from scipy.stats import shapiro

pop_data_shapiro = pop_data.drop('District', axis= 1)
#print(pop_data_shapiro)
#print(shapiro(pop_data_shapiro))

# if data skewed - spearmans
from scipy.stats import spearmanr

# calculate correlation and p value 
# cat ~ well-being correlations
#print(spearmanr(pop_data['cat owners'], pop_data['Life Satisfaction'])[0]) # <- rho (correlation)
#print(spearmanr(pop_data['cat owners'], pop_data['Life Satisfaction'])[1]) # <- p-value
#print(spearmanr(pop_data['cat owners'], pop_data['Anxiety'])[0])
#print(spearmanr(pop_data['cat owners'], pop_data['Anxiety'])[1])
#print(spearmanr(pop_data['cat owners'], pop_data['Worthwhile'])[0])
#print(spearmanr(pop_data['cat owners'], pop_data['Worthwhile'])[1])
#print(spearmanr(pop_data['cat owners'], pop_data['Happiness'])[0])
#print(spearmanr(pop_data['cat owners'], pop_data['Happiness'])[1])

# dog ~ well-being correlations
#print(spearmanr(pop_data['dog_owners'], pop_data['Life Satisfaction'])[0])
#print(spearmanr(pop_data['dog_owners'], pop_data['Life Satisfaction'])[1])
#print(spearmanr(pop_data['dog_owners'], pop_data['Anxiety'])[0])
#print(spearmanr(pop_data['dog_owners'], pop_data['Anxiety'])[1])
#print(spearmanr(pop_data['dog_owners'], pop_data['Happiness'])[0])
#print(spearmanr(pop_data['dog_owners'], pop_data['Happiness'])[1])
#print(spearmanr(pop_data['dog_owners'], pop_data['Worthwhile'])[0])
#print(spearmanr(pop_data['dog_owners'], pop_data['Worthwhile'])[1])

# Accounting for confounding variable -> population
# Total Population by region: 
pop_data['Population'] = [5447700, 
                          3131640,
                          6398497,
                          4934939,
                          8866180,
                          2683040,
                          7516113,
                          9379833,
                          5764881,
                          6021653,
                          5541262]

pop_data['cat_per_1000'] = (pop_data['cat owners'] / pop_data['Population'] * 1000)
pop_data['dog_per_1000'] = (pop_data['dog_owners'] / pop_data['Population'] * 1000)

#print(pop_data[['District', 'cat_per_1000', 'dog_per_1000']])

# cat ~ well-being correlations
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Life Satisfaction'])[0]) # <- rho (correlation)
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Life Satisfaction'])[1]) # <- p-value
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Anxiety'])[0])
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Anxiety'])[1])
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Worthwhile'])[0])
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Worthwhile'])[1])
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Happiness'])[0])
#print(spearmanr(pop_data['cat_per_1000'], pop_data['Happiness'])[1])

# dog ~ well-being correlations
print(spearmanr(pop_data['dog_per_1000'], pop_data['Life Satisfaction'])[0])
#print(spearmanr(pop_data['dog_per_1000'], pop_data['Life Satisfaction'])[1])
print(spearmanr(pop_data['dog_per_1000'], pop_data['Anxiety'])[0])
#print(spearmanr(pop_data['dog_per_1000'], pop_data['Anxiety'])[1])
print(spearmanr(pop_data['dog_per_1000'], pop_data['Happiness'])[0])
#print(spearmanr(pop_data['dog_per_1000'], pop_data['Happiness'])[1])
print(spearmanr(pop_data['dog_per_1000'], pop_data['Worthwhile'])[0])
#print(spearmanr(pop_data['dog_per_1000'], pop_data['Worthwhile'])[1])


#--------Simple Regression---------------------
# what is the direction and size of the association 

import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = pop_data[['dog_per_1000']]
y = pop_data['Anxiety']

model1 = LinearRegression()
model1.fit(X, y)

#print(f"Intercept: {model1.intercept_}")
#print(f"Coefficient: {model1.coef_}")


##-------------------------------------------------------
#RQ4: how do cats and dogs differ in their patterns of association with population well-being outcomes at the regional level?
# comparing direction and magnitude of the correlation coefficients obtained in RQ3
# instead of fitting the planned multiple linear regression model in order to avoid overfitting given small number of districts 


# create visual heatmap of effect sizes
heatmap_data = pd.DataFrame({'Cats (effect size)': [0.1272727272727273, -0.23636363636363636, 0.16363636363636366, 0.17272727272727276],
                             'Dogs (effect size)' : [-0.07272727272727274,-0.4272727272727273, 0.10909090909090911, -0.16363636363636366]}, 
                             index = ['Life Satisfaction', 'Anxiety', 'Happiness', 'Worthwhile'])


# rearranging variables 
heatmap_data = heatmap_data.loc[['Anxiety', 'Life Satisfaction', 'Worthwhile', 'Happiness']]

import seaborn as sns

plt.figure(figsize=(6,4))

sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap= "BuPu", center=0, linewidths=0.5)

plt.title("Comparing Patterns of Pet Ownership and Well-being (Spearman Correlation Effect Sizes (n = 11 UK Districts))")
plt.ylabel("Well-being Outcome")
plt.xlabel("Pet Type")
plt.figtext(0.1, 0, "Note: Values represent Spearman's rho. Colours represent direction and magnitude of association, not statistical significance.", color = "red", fontsize = 10)
plt.tight_layout
plt.show()

# import libraries necessary
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt

# read in file
sh_data = pd.read_csv('sh_data_all.csv', index_col=0)
#print(sh_data.head())

# exploratory data analysis

print(sh_data.describe())
# what did this tell us? there are 167 observations
# 50% percentile is less than the mean for sbq1, sbq2, sbq3, sbq4, sbq_total -> data is skewed to lower values


# get summary stats grouped by pet owner

summary_stats_by_pet_ownership = sh_data.groupby('pet_owner').mean()
#print(summary_stats_by_pet_ownership)
# summary stats showing that anxiety, depression and sbq answers lower with pet owners

# check datatypes
#print(sh_data.info()) # checking data type and non-null count

#----------------------------------------------------------------------------------------------
# 1. could do a scatterplot for anxiety and depression ratings based on pet ownership
# ---------------------------------SCATTERPLOTS-------------------------------------------

# 1. 

#x = sh_data['hads_anxiety']
#y = sh_data['hads_depression']
#colour = []

#for i in range(len(sh_data)):
    #if (sh_data['pet_owner'].iloc[i] == 0.0):
        #colour.append('violet')
    #elif (sh_data['pet_owner'].iloc[i] == 1.0):
        #colour.append('mediumslateblue')

#plt.scatter(x,y, c = colour)
#plt.legend(('No Pets', 'Pets'))
#plt.xlabel('Anxiety')
#plt.ylabel('Depression')
#plt.suptitle("Anxiety vs. Depression by Pet Ownership")
#plt.show()

#---------------------------------------------------------------
#ANOTHER WAY 

no_pets = sh_data[sh_data['pet_owner'] == 0.0]
pets = sh_data[sh_data['pet_owner'] == 1.0]

#plt.scatter(no_pets['hads_anxiety'], no_pets['hads_depression'], label = 'No Pets')
#plt.scatter(pets['hads_anxiety'], pets['hads_depression'], label = 'Pets')

#plt.xlabel('Anxiety')
#plt.ylabel('Depression')
#plt.suptitle('Anxiety vs. Depression by Pet Ownership')
#plt.legend()
#plt.plot()

#-----------------------------------------------------------------------------

# regression analysis - estimating one set based on the other
#from scipy import stats

#x = sh_data['hads_anxiety'].to_numpy().flatten()
#y = sh_data['hads_depression'].to_numpy().flatten()

#slope, intercept, r, p, std_err = stats.linregress(x,y)

#def myfunc(x):
 #   return slope * x + intercept

#mymodel = list(map(myfunc, x))

#plt.scatter(x, y)
#plt.legend()
#plt.plot(x, mymodel)
#plt.show()
#print(r)

#----------------------------------------------------------
# Research question 1
# multiple linear regression for anxiety

# print(sh_data.columns) -> checking column names

X = sh_data[['num_cat', 'num_dog']]
Y = sh_data['hads_anxiety']

from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(X, Y)

# checking for missing values - to be able to trust the model
##print(sh_data[['num_cat', 'num_dog', 'hads_anxiety']].isna().sum())

# viewing results:
#print("Intercept: ", regr.intercept_)
#print("Coefficients: ", regr.coef_)

coefficient_df_anxiety = pd.DataFrame({'Predictor': X.columns,
                               'Coefficient': regr.coef_})

#print(coefficient_df_anxiety)

r2 = regr.score(X, Y)
#print("R-Squared:", r2)

# multiple regression for depression
X = sh_data[['num_cat', 'num_dog']]
y = sh_data['hads_depression']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# viewing results:
#print("Intercept: ", regr.intercept_)
#print("Coefficients: ", regr.coef_)

coefficient_df_depression = pd.DataFrame({'Predictor': X.columns,
                               'Coefficient': regr.coef_})

#print(coefficient_df_depression)

r2 = regr.score(X, y)
#print("R-Squared:", r2)

#---------------------------------------------------------
# Research Question 2
# one-sample t-test 

from scipy.stats import ttest_ind
owners = sh_data.loc[sh_data['pet_owner'] == 1.0, 'sbq_total']
nonowners =  sh_data.loc[sh_data['pet_owner'] == 0.0, 'sbq_total']

t_stat, p_value = ttest_ind(owners, nonowners, equal_var= False)

#print(f"T-statistic: {t_stat:.4f}")
#print(f"P-value: {p_value:.4f}")

# get descriptive stats
#print(sh_data.groupby('pet_owner')['sbq_total'].agg(['mean', 'std']))

# Effect Size

import pingouin as pg 

d = pg.compute_effsize(owners, nonowners, eftype='cohen')
#print(f"Cohen's d: {d:.2f}")


#-------------------------------------------------------
#-------------------VISUALISATIONS------------------------

# RQ1 PLOTS:
import statsmodels.api as sm
import seaborn as sns
import numpy as np

# Coefficient Plot for Anxiety
# adding intercept
X_anxiety = sm.add_constant(sh_data[['num_cat', 'num_dog']])
y_anxiety = sh_data['hads_anxiety']

# build and fit the model
model_anxiety = sm.OLS(y_anxiety, X_anxiety)
results_anxiety = model_anxiety.fit()

# MSE of the residuals
print(f"MSE: {results_anxiety.mse_resid}")

# print regression summary 
print(results_anxiety.summary())

# define function to output plot of model coefficients

def coefplot(results_anxiety):

    # create a df of results summary
    coef_df = pd.DataFrame(results_anxiety.summary().tables[1].data)

    # add column names
    coef_df.columns = coef_df.iloc[0]

    # drop extra row with column labels 
    coef_df= coef_df.drop(0)

    # set index to variable names
    coef_df = coef_df.set_index(coef_df.columns[0])

    # change datatype from object to float
    coef_df = coef_df.astype(float)

    # drop the constant for plotting
    coef_df = coef_df.drop(['const'])

    # rename predictors
    coef_df = coef_df.rename(index = {'num_cat' : 'Number of Cats',
                                      'num_dog' : 'Number of Dogs'})

    # sort values by coef asc
    coef_df = coef_df.sort_values(by = ['coef'])

    ##plotting coefs##

    # y positions
    y_pos = np.arange(len(coef_df))

    # setting sns plot style to 'poster' making it wide on plot 
    sns.set_context("poster")

    # define figures, axes and plot
    fig, ax = plt.subplots(figsize = (10, 5))

    
    # error bars for 95% CI
    ax.errorbar(x= coef_df['coef'],y = y_pos, xerr = [coef_df['coef'] - coef_df['[0.025'],
                                                      coef_df['0.975]'] - coef_df['coef']], fmt = 'o', linestyle = 'none',
                                                        color = 'pink', ecolor = 'pink',capsize = 6)
    
    # coefficient points
    ax.scatter(coef_df['coef'], y_pos, color = 'pink', s = 10)
    
    
    # line to define zero on axis
    ax.axvline(0, linestyle = '--', color = 'red', linewidth = 1)


    # set title and labels 

    # y axis
    ax.set_yticks(y_pos)
    ax.set_yticklabels(coef_df.index)
    plt.tick_params(labelsize = 10)

    ax.set_title('Coefficients with 95% Confidence Intervals', fontsize = 15)
    ax.set_xlabel('')
    
    plt.tight_layout()
    return plt.show()

coefplot(results_anxiety)

#---------------------------------------------------
# Coefficient Plot for Depression
# adding intercept
X_depression = sm.add_constant(sh_data[['num_cat', 'num_dog']])
y_depression = sh_data['hads_depression']

# build and fit the model
model_depression = sm.OLS(y_depression, X_depression)
results_depression = model_depression.fit()

# MSE of the residuals
print(f"MSE: {results_depression.mse_resid}")

# print regression summary 
print(results_depression.summary())

# define function to output plot of model coefficients

def coefplot(results_depression):

    # create a df of results summary
    coef_df = pd.DataFrame(results_depression.summary().tables[1].data)

    # add column names
    coef_df.columns = coef_df.iloc[0]

    # drop extra row with column labels 
    coef_df= coef_df.drop(0)

    # set index to variable names
    coef_df = coef_df.set_index(coef_df.columns[0])

    # change datatype from object to float
    coef_df = coef_df.astype(float)

    # drop the constant for plotting
    coef_df = coef_df.drop(['const'])

    # rename predictors
    coef_df = coef_df.rename(index = {'num_cat' : 'Number of Cats',
                                      'num_dog' : 'Number of Dogs'})

    # sort values by coef asc
    coef_df = coef_df.sort_values(by = ['coef'])

    ##plotting coefs##

    # y positions
    y_pos = np.arange(len(coef_df))

    # setting sns plot style to 'poster' making it wide on plot 
    sns.set_context("poster")

    # define figures, axes and plot
    fig, ax = plt.subplots(figsize = (10, 5))

    
    # error bars for 95% CI
    ax.errorbar(x= coef_df['coef'],y = y_pos, xerr = [coef_df['coef'] - coef_df['[0.025'],
                                                      coef_df['0.975]'] - coef_df['coef']], fmt = 'o', linestyle = 'none',
                                                        color = 'pink', ecolor = 'pink',capsize = 4)
    
    # coefficient points
    ax.scatter(coef_df['coef'], y_pos, color = 'pink', s = 10)
    
    
    # line to define zero on axis
    ax.axvline(0, linestyle = '--', color = 'red', linewidth = 1)


    # set title and labels 

    # y axis
    ax.set_yticks(y_pos)
    ax.set_yticklabels(coef_df.index)
    
    # adjusting size of tick labels
    plt.tick_params(labelsize=10)

    ax.set_title('Coefficients with 95% Confidence Intervals', fontsize = 15)
    ax.set_xlabel('')
    
    plt.tight_layout()
    return plt.show()

coefplot(results_depression)





#Distribution of suicide risk: Histogram of SBQ scores

plt.hist(sh_data['sbq_total'], bins = 10, color="#EF95EF", edgecolor = 'black', alpha=0.5)
plt.xlabel("Suicide Risk Score (SBQ)")
plt.ylabel("Number of Participants")
plt.title("Distribution of Suicide Risk Scores")
#plt.show()

# Pet ownership and suicide risk: Boxplot

bp = plt.boxplot([nonowners, owners], tick_labels= ["No Pets", "Pet Owners"], patch_artist= True)

colours = [ "#519CCB","#C79FEF"]

for patch, colour in zip(bp['boxes'], colours):
    patch.set_facecolor(colour)
    patch.set_edgecolor("black")


for element in ['medians', 'whiskers', 'fliers', 'caps']:
    for item in bp[element]:
        item.set_color("black")

plt.ylabel("SBQ Total Score")
plt.title("Suicide Risk by Pet Ownership")
#plt.show()

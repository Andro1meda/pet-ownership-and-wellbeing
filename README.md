
<div align="center">

# 🌸 *Pet Ownership, Mental Health and Well-being Project* 🌸
⋆｡˚ ☁︎ ˚｡⋆｡˚ ☁︎ ˚｡⋆｡˚ ☁︎ ˚｡⋆｡˚ ☁︎ ˚｡⋆

</div>

## *Table of Contents* ࿔˚⋆
- [Project Overview](#project-overview-)
- [What this project demonstrates](#what-this-project-demonstrates)
- [Research Aim](#research-aim-)
- [Research Questions](#research-questions-)
  -  [Individual-Level Dataset](#individual-level-dataset)
  -  [Population-Level Dataset](#population-level-dataset)
- [Tools & Materials](#tools--materials-)
  -  [Data Sources](#data-sources)
  -  [Tech Stack](#tech-stack)
- [Analytical Workflow](#analytical-workflow-)
- [Findings](#findings-)
  - [Individual-Level Analysis](#individual-level-analysis)
  - [Population-Level Analysis](#population-level-analysis)
- [Lessons and Recommendations](#lessons-and-recommendations-)
- [Limitations and Improvements](#limitations-and-improvements-) 



## *Project Overview* ࿔˚⋆
This project demonstrates data wrangling, exploratory data analysis, statistical modelling, and visual storytelling using UK public datasets to investigate associations between pet ownership and mental well-being.

_*This project was completed independently outside of formal coursework_


## *What this project demonstrates*࿔˚⋆
- End-to-end data analysis using real-world public datasets
- Data cleaning and standardisation across multiple sources
- Exploratory data analysis (EDA) and statistical modelling
- Translating analytical findings into policy- and stakeholder-relevant insights

## *Research Aim* ࿔˚⋆
To examine the relationship between pet ownership and mental health and well-being at both the individual and population levels in the UK


## *Research Questions* ࿔˚⋆
### **_Individual-Level Dataset_**
- RQ1: Do cats or dogs differentially predict anxiety and depression symptoms at the individual level?
- RQ2:  What is the relationship between suicidal behaviours and pet ownership?

✦ ───────── ✦ ───────── ✦

### **_Population-Level Dataset_**
- RQ3: Are regional levels of cat and dog ownership associated with population well-being across UK districts?
- RQ4: How do cats and dogs differ in their patterns of association with population well-being outcomes at the regional level?


## *Tools & Materials* ࿔˚⋆
## **_Data Sources_**
- [ONS Personal well-being in the UK: April 2022 to March 2023](https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/bulletins/measuringnationalwellbeing/april2022tomarch2023)
- [Dog population per postcode district](https://www.data.gov.uk/dataset/ec8fc820-2e36-49d0-a09c-e2901e10b2e4/dog-population-per-postcode-district)
- [Cats Report 2022](https://www.readkong.com/page/cats-report-2022-cats-protection-8207642)
- [PFMA (pet food manufacturers’ association) UK pet data report 2022](https://ukpetfood-reports.co.uk/annual-report-2022/) _access to this report is only for membership now_
- [Pet Ownership and Self-Harm in UK Youth: Survey Dataset on Bond Quality, Self-Harm Behaviours, and Suicide Risk](https://doi.org/10.48420/29120819)
- [Estimates of the population for the UK, England, Wales, Scotland, and Northern Ireland - Mid-2022 Edition](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland)

## **_Tech Stack_**
- Excel
- Python
- _Libraries_: Matplotlib, Seaborn, Scikit-learn, Pandas, Numpy, SciPy

----
## *Analytical Workflow* ࿔˚⋆
1. Collected and validated multi-source public datasets
2. Cleaned and standardised pet ownership rates per capita
3. Conducted exploratory data analysis (EDA)
4. Built regression models to assess associations
5. Visualised and interpreted findings for non-technical audiences

## Findings ࿔˚⋆

**Key Takeaways**

Pet ownership was associated with better mental health at the individual level, particularly for depression and suicidal behaviours. However, no clear relationship was observed between pet ownership and population-level well-being across UK regions.

To Summarise:
- Individuals who owned pets reported better mental health
- Regions with more pets did not necessarily report better well-being overall


### Individual-Level Analysis


**What did we look at?**
We examined whether owning cats or dogs was related to:
- Anxiety
- Depression
- Suicidal thoughts and behaviours
_This was done using survey data from 167 individuals_


#### **Exploratory data analysis:**
- Descriptive statistics showed that in general pet owners reported lower anxiety and depression scores on average compared to non-pet owners. 

<img width="947" height="710" alt="image" src="https://github.com/user-attachments/assets/2910cce9-ed0d-4ab1-833f-e19dd11824ef" />

---

Research Question 1: Do cats or dogs differentially predict anxiety and depression symptoms at the individual level?

**_What does this mean?_**

This question tries to explore whether cats or dogs have different effects on anxiety and depression symptoms in individuals.

#### Anxiety

**What we found**
- Individuals with pets reported slightly lower anxiety
- However, the difference was very small
- There was not a difference between whether owning a cat or a dog would lower anxiety.

**What this means**  
Pet ownership alone does not appear to meaningfully reduce anxiety. Anxiety may be influenced by many other factors such as stress, finances, health, and other factors. 

**Why this matters**
- Pets should not be viewed as a standalone intervention for anxiety.
- Support services should continue to prioritise much broader psychological and social factors.


<img width="1490" height="716" alt="image" src="https://github.com/user-attachments/assets/ddc71951-7723-4897-8732-a52993490419" />

_This coefficient plot shows the estimated coefficients from the regression model - this helps to understand the significance and uncertainty of the relationship between variables_



#### Depression

**What we found** 
- Individuals who owned cats or dogs reported noticeably lower depression scores.
- The relationship was stronger and more meaningful than for anxiety.
- Cats and dogs contributed similarly to reduced depressive symptoms.

**What this means**    
Pet ownership may play a supportive role in protecting against depressive symptoms. This may be due to daily routines and responsibilities, companionship and emotional support, and reduced loneliness.

**Why this matters**
- Pets may act as preventative factors for mood-related well-being
- This is especially relevant for individuals at risk of social isolation.

<img width="1476" height="738" alt="image" src="https://github.com/user-attachments/assets/9a34c066-f428-4378-bc1b-46751576f2b8" />

_This coefficient plot for depression shows ..._


 ---
Research Question 2: What is the relationship between suicidal behaviours and pet ownership?

Method:

An independent sample t-test was conducted to compare suicidal behaviour scores between:
- non-pet owners
- pet owners
Suicidal behaviours were measured using the Suicidal Behaviours Questionnaire (SBQ) total score (sbq_total).
Effect size was calculated using Cohen's d.

Results:

Descriptive Statistics

|Pet Owner| SBQ Mean | SD|
|---------|------|-----|
|Non-Pet Owners |13.928571 | 3.789253|
|Pet Owners |11.756757  |4.600822|

Inferential Statistics  
$t$ = -3.25    
$p$ = 0.001  
Cohen's $d$ = -0.50

- Pet ownership is associated with lower levels of suicidal behaviours.
- Pet owners reported lower mean SBQ scores compared to non-pet owners.

<img width="936" height="693" alt="image" src="https://github.com/user-attachments/assets/bcd62774-c9a5-4c0a-a97e-0a32b441dbaa" />


Interpretation:  
Pet owners reported significantly lower suicidal behaviour scores than non-pet owners. The difference was statistically significant (p < .01) and represented a medium effect size, indicating a meaningful association between pet ownership and reduced suicidal behaviours.

The negative t-value and effect size reflect lower SBQ scores among pet owners, suggesting fewer suicidal thoughts, intentions, and future risk indicators.

---
Conclusion:  
At the individual level, pet ownership was associated with better mental health outcomes, though effects differed by outcome. The number of cats and dogs owned showed weak associations with anxiety, while pet ownership demonstrated a stronger relationship with depressive symptoms. Additionally, pet owners reported significantly lower suicidal behaviour scores than non-pet owners, with a moderate effect size.

Overall, these findings suggest that pet ownership is more strongly related to depression and suicidality than anxiety, highlighting its potential relevance for mood-related well-being at the individual level, while acknowledging that causal conclusions cannot be drawn from cross-sectional data.

### Population-Level Analysis
Dataset Overview:
- 11 observations
- Key Variables:
  - Pet Ownership:
    -  cat owners (number of cat owners)
    -  dog_owners (number of pet owners)
  - Well-being Outcomes:
    - Life Satisfaction
    - Happiness
    - Anxiety
    - Worthwhile
  - Regionality:
    - District

Research Question 3: Are regional levels of cat and dog ownership associated with population well-being across UK districts?

---

Method:  
Spearman's rank-order correlations were used to examine associations between regional pet ownership rates per 1000 residents and population well-being indicators (life satisfaction, happiness, worthwhileness, and anxiety). Spearman’s rho was selected due to non-normal distributions and ordinal properties after assumption checks.

Results:

Cats per 1000 residents  
|Well-being| Rho (&rho;) | $p$|
|-----------|------------|-----|
| Life Satisfaction| 0.13 | 0.71 |    
| Worthwhile | 0.17   | 0.61    |
| Anxiety | -0.24   | 0.48    |
|Happiness|  0.16  | 0.63    |


Dogs per 1000 residents
|Well-being| Rho (&rho;) | $p$|
|-----------|------------|-----|
| Life Satisfaction| -0.07    | 0.83    |
| Worthwhile| -0.16   | 0.63   |
| Anxiety | -0.43   | 0.19    |
|Happiness|  0.11  | 0.75   |

Interpretation:
At the population level, no statistically significant associations were observed between regional cat or dog ownership rates and well-being outcomes. Although some correlations suggested weak trends—such as higher dog ownership being associated with lower anxiety—these relationships were small and non-significant.



 
## Lessons and Recommendations ࿔˚⋆

## Limitations and Improvements ࿔˚⋆

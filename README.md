
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
  - [Individual-Level Analysis](#-individual-level-analysis)
  - [Population-Level Analysis](#-population-level-analysis)
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
## 📋**_Data Sources_**
- [ONS Personal well-being in the UK: April 2022 to March 2023](https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/bulletins/measuringnationalwellbeing/april2022tomarch2023)
- [Dog population per postcode district](https://www.data.gov.uk/dataset/ec8fc820-2e36-49d0-a09c-e2901e10b2e4/dog-population-per-postcode-district)
- [Cats Report 2022](https://www.readkong.com/page/cats-report-2022-cats-protection-8207642)
- [PFMA (pet food manufacturers’ association) UK pet data report 2022](https://ukpetfood-reports.co.uk/annual-report-2022/) _access to this report is only for membership now_
- [Pet Ownership and Self-Harm in UK Youth: Survey Dataset on Bond Quality, Self-Harm Behaviours, and Suicide Risk](https://doi.org/10.48420/29120819)
- [Estimates of the population for the UK, England, Wales, Scotland, and Northern Ireland - Mid-2022 Edition](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland)

## 💻**_Tech Stack_**
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


### 🔎Individual-Level Analysis


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

_**Research Question 1: Do cats or dogs differentially predict anxiety and depression symptoms at the individual level?**_

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

_This coefficient plot shows the estimated coefficients from the anxiety regression model - this helps to understand the significance and uncertainty of the relationship between variables. As both coefficients are on the left, this means they are negative (or reduce anxiety), however, as the confidence intervals are covering the red line this means it is not significant._



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

_This coefficient plot for depression shows both coefficient points for cats and dogs on the left side (negative), similar to anxiety. However, as ther are no confidence intervals touching the red line this means they are significant_


 ---
_**Research Question 2: What is the relationship between suicidal behaviours and pet ownership?**_

**What we found**  
- Pet owners reported significantly fewer suicidal thoughts and behaviours than non-pet owners.
- The difference was moderate in size, suggesting practical importance.

**What this means**  
Pet ownership may provide a number of benefits that helps buffer against suicidal risk. These may include emotional attachment, routine, and a sense of responsibility. 

**Why this matters**  
Pets, while not a substitute for mental health care, they may support recovery, reduce feelings of hopelessness and encourage help-seeking and routine. 

This finding is particularly relevant for suicide prevention strategies and youth and community mental health services. 

<img width="936" height="693" alt="image" src="https://github.com/user-attachments/assets/bcd62774-c9a5-4c0a-a97e-0a32b441dbaa" />


---
**Individual-Level Conclusion:**  
Individuals who own pets - in this case cats or dogs - tend to report better mental health, especially when it comes to depression and suicidal behaviours. However, the relationship with anxiety is weaker, suggesting pets are more helpful for mood and emotional support than for lowering anxiety.

---

### 🌐Population-Level Analysis

**What did we look at?**   
We examined whether UK regions with more cats or dogs per 1,000 residents, also reported:
- Higher life satisfaction
- Greater happiness
- Lower anxiety
- Greater sense of life being worthwhile

---

_**Research Question 3: Are regional levels of cat and dog ownership associated with population well-being across UK districts?**_

**What I found**
- There was no clear relationship between pet ownership rates and regional well-being.
- Some weak patterns appeared (e.g., dog ownership and lower anxiety), but they were not reliable or consistent.

<img width="1713" height="912" alt="image" src="https://github.com/user-attachments/assets/d7a85c89-4b17-4935-bc35-815a55ae1b43" />


**What this means**  
Having more pets owned in a region or district does not automatically translate into better population well-being. This suggests that community well-being may depend more on other factors such as: economic status, access to healthcare, social inequality, housing and environments and other factors. 
Therefore, the mental health and well-being benefits of owning a pet are more personal, rather than structural.

---
**Population-Level Conclusion:**  
While pets appear beneficial for individuals, increasing pet ownership at the regional level alone is unlikely to improve population-wide well-being.

---
 
## Lessons and Recommendations ࿔˚⋆

**What this project shows** 

- Pets may act as a protective personal resource for well-being
- Their impact is strongest at the individual level
- They should be seen as supportive, not curative

📋**Recommendations**
Mental Health Services
- Consider pet ownership as a protective factor during assessments

Assisted Interventions
- Investigate animal-assisted or companion-based interventions

Community
- Support responsible pet ownership, especially for isolated individuals

Policy-makers
- Address wider inequalities and avoid assuming that higher pet ownership improves population mental health and well-being

## Limitations and Improvements ࿔˚⋆

☁️**Limitations**

- Use of cross-sectional data: although shows uses of different data sources in a project, it cannot prove cause and effect
- Small sample sizes: only had 11 observations, as it was an investigation into regional levels of well-being
  - Also, due to ONS Well-being factors not including Northern Ireland, Northern Ireland was not included in this analysis.
- Self-reported mental health and well-being measures: introduces further bias in the data
- Secondary survey data was used for this project, therefore some variables were not able to be controlled, such as gender and ethnicity, as it was not clear what the values represented
- Additionally, there was no data on: quality of pet-owner bond, length of ownership, living conditions, and social economic status, which were variables that may influence the findings

🔮**Future Improvements**

- Longitudinal research designs
Future studies should track changes of well-being and mental health measures over time in pet and non-pet owners, allowing for stronger inferences about directionality and long-term effects.

- Larger and more granular samples
Rather than aggregating UK areas into districts prior to analysis, future work could retain area-level data with an added district identifier, allowing findings to be aggregated post-analysis. This would preserve regional variability and improve statistical sensitivity.

- Inclusion of bond quality and caregiving burden
Including measures of emotional attachment, responsibility, and caregiving demands would help distinguish when pet ownership is protective versus when it may introduce stress.

- Qualitative interviews to capture lived experience
Interviews or open-ended survey responses could provide further insight into how individuals experience pet ownership in relation to mental health, complementing quantitative findings.

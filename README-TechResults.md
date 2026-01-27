## 🌸Technical Results

**Dataset Overview**:
- Sample size: 167 participants
- Key variables:
  - Mental Health outcomes:
    - hads_anxiety _(anxiety scores from the Hospital Anxiety and Depression Scale (HADS))_
    - hads_depression  _(depression scores from the Hospital Anxiety and Depression Scale (HADS))_
    - sbq_total _(overall scores from the Suicidal Behaviours Questionnaire)_
  - Pet ownership indicators:
    - num_cat _(number of cats owned)_
    - num_dog _(number of dogs owned)_
    - pet_owner _(if participant is a pet owner or not)_
   
*Exploratory data analysis indicated that suicidality scores were positively skewed, with most participants reporting low levels. Descriptive statistics suggested that pet owners reported lower anxiety and depression on average compared to non-pet owners. 


<img width="947" height="710" alt="image" src="https://github.com/user-attachments/assets/2910cce9-ed0d-4ab1-833f-e19dd11824ef" />

---


_**Research Question 1: Do cats or dogs differentially predict anxiety and depression symptoms at the individual level?**_

**Method:**  
- Two mulitple linear regression models were conducted:
  - Model 1: Predicting anxiety (hads_anxiety)
  - Model 2: Predicting depression (hads_depression)
- Predictors:
  - Number of cats owned (num_cat)
  - Number of dogs owned (num_dog)
 
**Results:**

Model 1: Anxiety  

|Predictor   | Coefficient|
|-------------|-----------|
|Intercept   | 13.80|
|No. of cats | -0.67|
|No. of dogs | -0.27|

$R^2$ = 0.02
- Both cats and dogs showed small negative associations with anxiety.
- This model explained approximately 2% of the variance, indicating a weak relationship.

<img width="1490" height="716" alt="image" src="https://github.com/user-attachments/assets/ddc71951-7723-4897-8732-a52993490419" />


**Interpretation:**  
While pet ownership was associated with slighly lower levels of anxiety, the model showed a low effect size, suggesting that anxiety is largely explained by factors beyond pet ownership.

Model 2: Depression
|Predictor   | Coefficient|
|-------------|----------|
|Intercept   | 12.39|
|No. of cats | -1.57|
|No. of dogs | -1.63|

$R^2$ = 0.14
- Owning more cats or dogs was associated with lower depression scores.
- The model explained approximately 14% of the variance, which is moderate for psychological data.



<img width="1476" height="738" alt="image" src="https://github.com/user-attachments/assets/cf7bc592-f4a5-422b-b404-b5e8617c4941" />


**Interpretation:**   
Pet ownership showed a stronger and more meaningful association with depression than anxiety, with cats and dogs contributing similarly to reduced depressive symptoms.

 ---

_**Research Question 2: What is the relationship between suicidal behaviours and pet ownership?**_


**Method:**  

An independent sample t-test was conducted to compare suicidal behaviour scores between:
- non-pet owners
- pet owners
Suicidal behaviours were measured using the Suicidal Behaviours Questionnaire (SBQ) total score (sbq_total).
Effect size was calculated using Cohen's d.

**Results:**

_Descriptive Statistics_

|Pet Owner| SBQ Mean | SD|
|---------|------|-----|
|Non-Pet Owners |13.928571 | 3.789253|
|Pet Owners |11.756757  |4.600822|

_Inferential Statistics_  
$t$ = -3.25    
$p$ = 0.001  
Cohen's $d$ = -0.50

- Pet ownership is associated with lower levels of suicidal behaviours.
- Pet owners reported lower mean SBQ scores compared to non-pet owners.

<img width="936" height="693" alt="image" src="https://github.com/user-attachments/assets/bcd62774-c9a5-4c0a-a97e-0a32b441dbaa" />


**Interpretation:**  
Pet owners reported significantly lower suicidal behaviour scores than non-pet owners. The difference was statistically significant (p < .01) and represented a medium effect size, indicating a meaningful association between pet ownership and reduced suicidal behaviours.

The negative t-value and effect size reflect lower SBQ scores among pet owners, suggesting fewer suicidal thoughts, intentions, and future risk indicators.


**Conclusion:**  
At the individual level, pet ownership was associated with better mental health outcomes, though effects differed by outcome. The number of cats and dogs owned showed weak associations with anxiety, while pet ownership demonstrated a stronger relationship with depressive symptoms. Additionally, pet owners reported significantly lower suicidal behaviour scores than non-pet owners, with a moderate effect size.

Overall, these findings suggest that pet ownership is more strongly related to depression and suicidality than anxiety, highlighting its potential relevance for mood-related well-being at the individual level, while acknowledging that causal conclusions cannot be drawn from cross-sectional data.

---

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
---

_**Research Question 3: Are regional levels of cat and dog ownership associated with population well-being across UK districts?**_


**Method:**  
Spearman's rank-order correlations were used to examine associations between regional pet ownership rates per 1000 residents and population well-being indicators (life satisfaction, happiness, worthwhileness, and anxiety). Spearman’s rho was selected due to non-normal distributions and ordinal properties after assumption checks.

**Results:**


_Cats per 1000 residents_

|Well-being| Rho (&rho;) | $p$|
|-----------|------------|-----|
| Life Satisfaction| 0.13 | 0.71 |    |
| Worthwhile | 0.17   | 0.61    |
| Anxiety | -0.24   | 0.48    |
|Happiness|  0.16  | 0.63    |


_Dogs per 1000 residents_

|Well-being| Rho (&rho;) | $p$|
|-----------|------------|-----|
| Life Satisfaction| -0.07    | 0.83    |
| Worthwhile| -0.16   | 0.63   |
| Anxiety | -0.43   | 0.19    |
|Happiness|  0.11  | 0.75   |

<img width="1713" height="912" alt="image" src="https://github.com/user-attachments/assets/d7a85c89-4b17-4935-bc35-815a55ae1b43" />



**Interpretation:**
At the population level, no statistically significant associations were observed between regional cat or dog ownership rates and well-being outcomes. Although some correlations suggested weak trends—such as higher dog ownership being associated with lower anxiety—these relationships were small and non-significant.

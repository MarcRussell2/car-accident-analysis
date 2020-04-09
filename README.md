# car-accident-analysis
---------------------
# setup car accident dataset
clean dataset from where
show date range
show number of rows and columns
show column with meaning and examples


# state vs state
how many states of data
best state
worst states

# weather analysis
how many weather conditions in dataset
meaning of weather stamps
any correlation to weather?
rates/distance/severity

# map images
view denver dangerous roads
view new york overlay map boroughs
allow people to go find their accidents

# time of day analysis
what are the safest and most dangerous times of day?
unable to normalize (rush hour spikes)


# Car Accidents Analysis

<p align="center">
  <img src="main/img/road_line_mnt.png" width = 900 height = 80>
</p>

## Effects of Location, Weather, and Time on Accident Rate and Severity in the United States

*Capstone I Project for Galvanize Data Science Immersive, Week 4*

*by Marc Russell*


## Table of Contents
- [Introduction](#introduction)
  - [Background](#background)
  - [The Data](#the-data)
  - [Question and Hypothesis](#question-and-hypothesis)
  - [Methodology](#methodology)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Selection](#model-selection)
  - [Test Metric: F1 Score](#test-metric-f1-score)
  - [Feature Selection](#feature-selection)
  - [Hyperparameter Tuning](#hyperparameter-tuning)
- [Chosen Model](#chosen-model)
  - [Specifications](#specifications)
  - [Model Assessment](#model-assessment)
  - [Results and Interpretation](#results-and-interpretation)
- [Conclusion](#model-selection)
- [Citation](#citation])


# Introduction

## Background

A

## The Data

The University of Minho'


## Question and Hypothesis

For now, it 

Can we predict a student's relationship statuse and outcomes?

MVP
1. Encode fe via logistic regression
2. Levemodel/feature selection
3. Using th

## Methodology

<p align="center">
  img src="images/methodology.png" width = 800
</p>

[Back to Top](#Table-of-Contents)

# Exploratory Data Analysis

### Groups

* 395 students in Math courses

### Feature Categories

* Demographic Characteristics:

       school, sex, age, address, traveltime, internet, health

* Social Connection:

      famsize, Pstatus, Medu, Fedu, Mjob, Fjob, reason, guardian, schoolsup, famsup, paid, nursery, famrel, goout, Dacl, Walc

* Eductional Performance and Outcomes:

      studytime, failures, activities, higher, freetime, romantic, G1, G2, G3, absences


n see from both of these plots, the grade features (G1, G2, and G3) are strongly correlated. Since these variables each represent a given students' grade in the class at different periods throughout the year, it seems reasonable to simply use the final grade (G3) for the purposes of this analysis.

### Final Grade Distributions by Relationship Status

<p align="center">
  img src="images/p_g3_dist.png" width = 400
</p>


[Back to Top](#Table-of-Contents)

# Model Selection

## Feature Selection
Evaluating the performance of 3 models with varying features:

    1. Full model uses all 69 predictors
    2. Secondary model uses 29 predictors, using demographic and educational performance features
    3. Third model uses 18 predictors, focusing on educational outcomes only

## Hyperparameter Tuning 
Used SKLearn's GridSearch to find the best values for the following hyperparameters.

| Hyperparameter | Math Dataset Optimal Value | Portuguese Dataset Optimal Value |
|---|---|---|
| penalty | 'l1' | 'l2' |
| C (inverse of regularization param) | 7.743 | 1.0 |

[Back to Top](#Table-of-Contents)

# Chosen Model

## Specifications
    threshold=0.5
    class_weight = 'balanced'
    penalty = l1 (MATH), l2 (PORTUGUESE)
    C = 7.742636826811269 (MATH), 1.0 (PORTUGUESE)

For both Math and Portuguese students, the 3rd model that I tested performed the best, which contained only features on educational outcomes.

## Model Assessment

### Portuguese Data Confusion Matrix
<p align="center">
  img src="images/p_conf_mat.png" width = 400
</p>


## Results and Interpretation

### Change in Odds of Being in a Relationship
ghjfghj

[Back to Top](#Table-of-Contents)

# Conclusion
It does seem that there is a statistically significant difference between students who are in a relationship and those who are not for certain educationnity.  

[Back to Top](#Table-of-Contents)

# Citation
*Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.*

*Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.*

*http://worldpopulationreview.com/states/*

*(dataset) USDA Economic Research Service. (2020). Atlas of Rural and Small-Town America. Ag Data Commons. https://data.nal.usda.gov/dataset/atlas-rural-and-small-town-america. Accessed 2020-04-08.*

*Photo by Jeremy Bishop on Unsplash*

*Photo by sergio souza on Unsplash*

[Back to Top](#Table-of-Contents)

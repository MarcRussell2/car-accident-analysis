*Capstone I Project for Galvanize Data Science Immersive, Week 4*

*by Marc Russell*

# Car Accidents Analysis

<p align="center">
  <img src="main/img/road_line_mnt.png" width = 900 height = 80><sup>(2)</sup>
</p>

## Effects of Location, Weather, and Time on Accident Rate and Severity in the United States

## Table of Contents
- [Introduction](#introduction)
  - [Motivation](#motivation)
  - [The Data](#the-data)
  - [Questions](#questions)
- [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Dataset Overview](#dataset-overview)
  - [Feature Categories](#feature-categories)
  - [Exploration](#exploration)
    - [Weather](#weather)
    - [Location](#location)
    - [State](#state)
    - [Time](#time)
- [Conclusion](#conclusion)
- [Citation](#citation)


# Introduction

## Motivation

Through careful analysis of historical automobile accidents, I believe we can greatly reduce what is the biggest killer of young adults in this country.<sup>(3)</sup> The amount of money, time, and lives lost to car accidents is something that concern all of us and is worth spending time analyzing.

## The Data

The car accident dataset has been collected in real-time, using multiple Traffic APIs. It contains car accident data that is collected from February 2016 to December 2019 for the contiguous United States. By using several data providers such as the US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors within the road-networks, the authors<sup>(1)</sup> were able to construct about 3 million detailed accident records. This comprises somewhere between 10% and 50% of the total number of accidents in the US during that time span.

The population dataset was an annual report given out by the IRS which describes precisely the number and amounts of many tax details including income, population, etc. for each US Zipcode.
 

## Questions

 - How does weather (temperature, wind, precipitation, visibility, etc.) effect accident rates? <sup>MVP.1</sup>

 - What are the safest states to drive in?  <sup>MVP.1</sup>
 
 - When are the safest times of the day/month/year to drive?  <sup>MVP.1</sup>
 
 - Do higher income neighborhoods have lower accident rates? <sup>MVP.3</sup>

 - Do neighborhoods with high education taxes have lower accident rates? <sup>MVP.3</sup>

 - Are accident rates lower in towns with more farms? <sup>MVP.3</sup>

 - How does unemployment effect accident rates? <sup>MVP.3</sup>

 - How does number of retirees effect accident rates? <sup>MVP.3</sup>


MVP (Minimum Viable Product)
1. Exploratory data analysis & plots
2. Geolocational map images, interactive maps
3. Combine tax datasets to discover relations between income/education/unemployment/farms and accident rates


[Back to Top](#Table-of-Contents)

# Exploratory Data Analysis

## Dataset Overview

Accident Dataset:
 - 49 columns and 3 million rows
 - Columns describe the accident event
 - Each row is a unique accident event
 
IRS Dataset:
 - 153 columns and 1 million rows
 - Each Column is an amount for each tax variable
 - Each Zipcode has 6 rows (one for each income division)

## Feature Categories


* Accident Results:

       Accident Counts (rows), Severity, Length of Road Effected, Description

* Weather:

      Temperature, Weather Condition, Precipitation, Visibility

* Road Attributes:

      Nearby Traffic Signs (Yield, Stop, etc.), Railroads, Speed Bumps, Merges
      
* Geo-positional:

      Latitude, Longitude, State, County, City, Zipcode


## Exploration

### Weather

#### Weather Condition: 
A naive analysis of how the weather conditions relate to accident counts would show that there is no significant increase in accident counts during precipitation. By plotting a histogram of the weather condition counts we don't take into consideration that weather conditions are not identically distributed. 
For example, if it doesn't snow often but there is a high accident rate when it snows, then we will not be able to see this by only observing the accident counts; the snow-accidents are eclipsed by the large number of non-snow-accidents.

<p align="center">
  <img src="main/img/weather_vs_count.png" width = 600>
</p>

#### Temperature: 
Does temperature correlate with number of accidents? Is there a spike below 32<sup>o</sup>F?

<p align="center">
  <img src="main/img/temp_counts.png" width = 600>
</p>

Comparing temperature to the number of accidents showed no significant increase at 32<sup>o</sup> F. The plot seems to have a right skew which further backs our assumption earlier - the data is not independent and identically distributed over all temperatures.


#### Precipitation: 
Taking a look at the precipitation amount against the number of accidents we notice two areas of interest. 

<p align="center">
  <img src="main/img/precip_counts.png" width = 600>
</p>

For small amounts of precipitation, we notice a steep decline as precipitation increases. For precipitation near 10 inches per hour we see a significant increase in accident counts. This is likely a result of the human psychological tendency to prefer 'round' numbers; this is often referred to as 'round number bias'.

#### Visibility: 
Does visibility negatively correlate with number of accident?

<p align="center">
  <img src="main/img/visibility_counts.png" width = 600>
</p>

No, there may be a positive correlation but it is inconclusive.

The weather data proved difficult to adjust due to underlying data distributions. An example from above is how weather conditions distribute themselves. If this distribution in not uniform, or if we do not subtract it out, we will not be able to obtain meaningful results. With this in mind, I moved onto other features that I knew I could eliminate their underlying distributions.

### Location

The locations of each accident were precisely recorded using geo-positional data (latitude and longitude). These locations allowed for easy mapping of the national roads. Below you can see some heat-map style accident-maps on some popular U.S. areas.

<p align="center">
  <img src="main/img/cali_map1.png" width = 430>
  <img src="main/img/nyc_map1.png" width = 400>
  <img src="main/img/denver_map1.png" width = 700>
</p>

#### State:

I quickly became interested in comparing accident counts between states to determine the most and least 'dangerous' states to drive in.  To avoid the naive mistakes mentioned above we will be adjusting the accident counts. One way to adjust the number-of-accidents-per-state is to divide by the state population. This is the approach I will be taking below. 

It's important to distinguish the difference before and after the adjustment on number of accidents. The 'unadjusted' graphs below represent the number of accidents for each state over 3.5 years. These values are weighted since each state has a different number of drivers. To remove this population-bias we can divide each state's number of accidents by the population of that state (assumed to be proportional to the # of drivers); dividing by 3.5 will give us a per-year rate. After these adjustments, our value represents the number of accidents per person per year in each state; we will refer to as the *accident rate* from now on.

<p align="center">
  <img src="main/img/state_acc_count_rate.png" width = 850>
</p>

Top-left notice how California's large population outweighs South Carolina's number of accidents despite there being a lower accident rate in California.

### Time:

Let's take a look at how accident counts change throughout the day. 

<p align="center">
  <img src="main/img/accident-count-throughout-the-day-3.png" width = 700>
</p>

As we expected there are two peaks in accident counts, one for each 'rush hour'. Let's instead look at how accident counts change over large time scales.

Plotting over the entire year of 2017 there are two features that stand out. There are many short-term fluctuation as well as a single, longer-term increase in accident counts. The long term fluctuation occurs near the fall equinox. One cause of this could be wet leaves on the roads - a serious hazard.

<p align="center">
  <img src="main/img/accident-count-throughout-the-year.png" width = 700>
</p>

Let's examine the shorter-term fluctuations. If we were to count the peaks or valleys, we would find that there are about 52 - suggesting that it is weekly.

<p align="center">
  <img src="main/img/accident-count-throughout-april.png" width = 700>
</p>

Above I have zoomed into a single month (April of 2017) and shaded the weekends. It's quite apparent that there are many more accidents during the week (Monday - Friday) than the weekend (Saturday, Sunday). As mention previously, the number of drivers on the road may be much higher during the week causing the plot above to be 'weighted'. Because of this, it is not appropriate to compare accident *counts* from different times of the day.

[Back to Top](#Table-of-Contents)


# Conclusion

I initially wanted to focus my study on how weather conditions effect accident rates. It turned out that adjusting my data to account for the fact that is not independent and identically distributed (IID) proved difficult. To remedy this, I would source a dataset of locational-hourly-weather and merged with the accident data set. Instead I decided to shift focus to exploring how accident counts change with location.

I found the relationships of state-to-state accident rates very interesting. Despite the data not being IID I was able to merge a population dataset with the accident counts to achieve a rate - the number of accidents per person per year in each state. This subtle change allows us to compare states between each other despite variable populations. It turns out that South Carolina has the highest accident rate while North and South Dakota have the lowest accident rates.

Lastly I looked at the relationship between time and accident counts. It quickly became apparent that the accident counts over time were also not IID. I decided to explore the relationship anyway, being careful not to draw strict conclusions. Over the course of the day it was expected to see the double rush hour peak. On the other hand, I found it surprising that the seasonal rise in accident counts happened during fall and not winter. 

I hope to return to this dataset soon and explore the remaining corners. It will also be a fun challenge to merge the aforementioned dataset which will allow me to draw conclusions where I was not able to before.

[Back to Top](#Table-of-Contents)

# Citation

<sup>(1)</sup>*Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019. https://www.kaggle.com/sobhanmoosavi/us-accidents*

*Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.*

<sup>(2)</sup>*Photo by sergio souza on Unsplash*

<sup>(3)</sup>*Deaths are from the National Center for Health Statistics (NCHS), except 1964, which are National Safety Council (NSC) estimates based on data from the National Highway Traffic Safety Administration’s (NHTSA) Fatality Analysis Reporting System (FARS) https://injuryfacts.nsc.org/motor-vehicle/historical-fatality-trends/deaths-and-rates*

*http://worldpopulationreview.com/states*

*USDA Economic Research Service. (2020). Atlas of Rural and Small-Town America. Ag Data Commons. https://data.nal.usda.gov/dataset/atlas-rural-and-small-town-america. Accessed 2020-04-08.*



*National Center for Statistics and Analysis. (2017, October). 2016 fatal motor vehicle crashes: Overviewexternal icon. (Traffic Safety Facts Research Note. Report No. DOT HS 812 456). Washington, DC: National Highway Traffic Safety Administration.*

[Back to Top](#Table-of-Contents)

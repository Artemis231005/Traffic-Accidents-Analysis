# Traffic Accidents Analysis for Identification of High-Risk Factors & Improving Road Safety

## Introduction

This project analyzes **traffic accident data** in **Delhi** to identify patterns, trends and risk factors influencing road safety using **exploratory data analysis (EDA)**. It aims to identify how frequency and severity of accidents vary with time, vehicle type, environmental conditions as well as human behavior.

---

## Data Sources

- Official Delhi Police Traffic Data (2021–2023): 
  - Dataset 1 provides statistics on fatalities and injuries across road user categories, Dataset 2 provides information across vehicle types.
  - Link: https://data.opencity.in/dataset/delhi-road-crashes-data

- Accident Dataset with Cause Columns:
  - Includes detailed attributes such as weather conditions, lighting, speed, driver impairment and post-crash response time.
  - Link: https://reportmedic.org/tools/india-datasets.html

---

## Tools & Libraries

* Python
* Pandas
* Numpy
* Matplotlib

---

## Data Cleaning & Preprocessing

* Reshaped wide formatted dataset using melt()
* Verified absence of anomalies such as null values and duplicates
* Converted categorical flags into meaningful labels
* Parsed time data to extract hourly patterns
* Binned continuous variables (post-crash care time) into ranges

---

## Analysis Performed

* Year-wise trend of fatalities and injuries
*  Vehicle type vs crash type and frequency analysis
* Category-wise comparison of vehicle types
* Impact of weather and lighting conditions on crashes
* Influence of behavioral factors such as driver impairment, seatbelt usage
* Time-of-day accident distribution
* Post-crash emergency response analysis

---

## Key Insights

* Fatalities and injuries peaked in **2022**, with slight increase afterward
* **Pedestrians** and **two-wheeler riders** are the most vulnerable groups
* **Private** and **vehicles carrying goods** account for the highest number of crashes
* **Hazy** and **rainy weather** conditions show higher accident frequency
* **Night-time** but **well-lit** conditions have highest accident rates
* **Driver impairment** and **lack of seatbelt use** increase fatality risk
* Peak accident time occurs around the afternoon at **15:00–16:00**

---

## Limitations

* Official datasets lack detailed feature-level data and tabular row data, providing aggreagates
* Limited to a small time span of 2021–2023
* Some variables (such as speed) may not fully reflect real world scenario
* Dataset scope is limited to a specific region


# Seasonal Agriculture Performance Analysis 🌾

### VOIS AICTE Batch 2026–2027 — Major Project

A **Data Analytics project** that investigates how agricultural performance varies across the **Kharif, Rabi, and Zaid seasons** using a dataset containing 4,000 farm records.

The project analyzes environmental conditions, farming inputs, crop productivity, irrigation practices, and economic outcomes to identify meaningful seasonal patterns and relationships.

---

##  Problem Statement

Agricultural activities are influenced by seasonal variations in environmental conditions, farming practices, resource availability, and market conditions.

Raw agricultural data does not directly reveal how agricultural performance changes between seasons or which factors are associated with better agricultural and economic outcomes.

This project focuses on analyzing the available agricultural data to:

* Compare performance across seasons
* Identify seasonal trends and patterns
* Examine environmental conditions
* Analyze resource and input usage
* Compare crop and irrigation performance
* Investigate relationships between variables
* Evaluate seasonal differences statistically
* Generate evidence-based agricultural insights

---

##  Objectives

The main objectives of the project are to:

* Explore and understand the agricultural dataset
* Clean and prepare the data for analysis
* Compare agricultural performance across seasons
* Identify important seasonal patterns and trends
* Analyze relationships between environmental conditions and agricultural outcomes
* Compare crops, states, and irrigation methods
* Apply statistical techniques to evaluate seasonal differences
* Visualize important patterns and relationships
* Interpret findings based on the available data
* Develop data-driven recommendations

These objectives are aligned with the VOIS AICTE project requirements for investigating seasonal patterns, relationships, variations, and agricultural outcomes.

---

##  Dataset

The dataset contains **4,000 farm records** covering different seasons, states, crops, irrigation methods, environmental conditions, agricultural inputs, and economic outcomes.

### Seasons

* Kharif
* Rabi
* Zaid

### States

* Andhra Pradesh
* Maharashtra
* Telangana
* Karnataka
* Gujarat
* Tamil Nadu
* Punjab
* Madhya Pradesh

### Crops

* Wheat
* Maize
* Pulses
* Rice
* Cotton
* Chilli
* Groundnut
* Sugarcane

### Irrigation Methods

* Drip
* Flood
* Rainfed
* Sprinkler

### Data Categories

**Environmental**

* Rainfall
* Temperature
* Humidity
* Soil health
* Soil moisture

**Agricultural Inputs**

* Fertilizer usage
* Pesticide usage
* Irrigation
* Water usage
* Seed quality

**Agricultural Outcomes**

* Yield
* Disease/pest risk

**Economic Outcomes**

* Production cost
* Revenue
* Profit

---

##  Key Questions

The analysis investigates questions such as:

1. How does agricultural performance vary across Kharif, Rabi, and Zaid?
2. Which season has the strongest overall performance?
3. How does crop yield vary across seasons?
4. How does profitability change between seasons?
5. Which irrigation method performs best?
6. What environmental factors are associated with yield?
7. How does resource usage differ across seasons?
8. Which states and crops show stronger economic performance?
9. Are seasonal differences statistically significant?
10. Are the observed seasonal patterns consistent across crops and regions?

These questions are based on the analytical areas suggested in the VOIS project brief, including seasonal performance, environmental conditions, resource usage, economic outcomes, regional variation, and unexpected patterns.

---

##  Methodology

### 1. Data Cleaning

The dataset was inspected and prepared before analysis.

Missing values in:

* Rainfall
* Soil moisture
* Yield

were handled using **season-wise median imputation** to preserve the seasonal characteristics of the data.

Potential outliers were also examined to determine whether they represented genuine observations before deciding whether they should be retained.

---

### 2. Exploratory Data Analysis

Descriptive statistics were calculated to understand how agricultural and economic variables change across seasons.

The analysis examined:

* Yield
* Rainfall
* Temperature
* Humidity
* Soil conditions
* Cost
* Revenue
* Profit
* Disease/pest risk
* Resource usage

---

### 3. Seasonal Comparison

Agricultural performance was compared across:

* Kharif
* Rabi
* Zaid

Additional comparisons were performed across:

* Crops
* States
* Irrigation methods

Grouped summaries and pivot-based analysis were used to identify differences between categories.

---

### 4. Statistical Analysis

One-way **ANOVA** was used to determine whether differences in agricultural performance between seasons were statistically significant.

The analysis specifically examined:

* Yield
* Profit

---

### 5. Correlation Analysis

Correlation analysis was performed to investigate relationships between environmental conditions, agricultural inputs, yield, and profit.

This helped identify variables that showed stronger or weaker associations with agricultural performance.

---

### 6. Data Visualization

The analysis uses visualizations to communicate important patterns, including:

* Bar charts
* Boxplots
* Correlation heatmaps
* Stacked charts
* Seasonal comparisons

---

##  Technologies Used

* **Python 3**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **SciPy**
* **VS Code**

---

##  Repository Structure

```text
Seasonal-Agriculture-Performance-Analysis/
│
├── seasonal_agriculture_performance_dataset.csv
│   └── Source agricultural dataset
│
├── Seasonal_Agriculture_Performance_Analysis.py
│   └── Complete Python analysis
│
├── README.md
│   └── Project overview, methodology and setup
│
├── FINDINGS.md
│   └── Detailed analytical findings and recommendations
│
└── VOIS_Major_Project_PPT_Filled.pptx
    └── Project presentation
```

---

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Rakshitha-52/seasonal_crop_analysis.git
cd Seasonal-Agriculture-Performance-Analysis
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy
```

### 3. Place the dataset

Make sure the following file is present in the project directory:

```text
seasonal_agriculture_performance_dataset.csv
```

### 4. Run the analysis

The project was developed and executed using **VS Code**.

Run:

```bash
python Seasonal_Agriculture_Performance_Analysis.py
```

The script performs the data preparation, analysis, statistical testing, and visualization steps.

---

##  Results

The analysis identifies several notable seasonal patterns, particularly in **profitability, irrigation performance, crop performance, water usage, and regional differences**.

For the complete results, statistical findings, interpretation, and recommendations, see:

###  [FINDINGS.md](FINDINGS.md)

---

##  Project Documentation

The repository separates the project into two main documentation layers:

**README.md**
Provides the project overview, problem statement, objectives, dataset, methodology, tools, and instructions for running the analysis.

**FINDINGS.md**
Documents the analytical results, statistical tests, major observations, interpretations, and recommendations.

This structure keeps the project overview concise while providing a dedicated place for the detailed analytical findings.

---

##  Author

**Rakshitha**

VOIS AICTE Batch 2026–2027
Major Project — Data Analytics

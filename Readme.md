Seasonal Agriculture Performance Analysis

VOIS AICTE Batch 2026–2027 — Major Project Data Analytics project investigating how agricultural performance varies across seasons (Kharif, Rabi, Zaid) using a 4,000-record farm dataset.

Problem Statement

Agricultural activities are influenced by seasonal variations in environmental conditions, farming practices, resource availability and market conditions. Raw agricultural data does not, by itself, reveal how performance changes across seasons. This project cleans and analyzes the dataset to uncover meaningful seasonal patterns, trends, relationships and differences in agricultural performance, and turns those findings into evidence-based recommendations.

Dataset
	
File	seasonal_agriculture_performance_dataset.csv
Records	4,000 farms
Seasons	Kharif, Rabi, Zaid
States	Andhra Pradesh, Maharashtra, Telangana, Karnataka, Gujarat, Tamil Nadu, Punjab, Madhya Pradesh
Crops	Wheat, Maize, Pulses, Rice, Cotton, Chilli, Groundnut, Sugarcane
Irrigation methods	Drip, Flood, Rainfed, Sprinkler
Fields	Environmental conditions (rainfall, temperature, humidity, soil health), input usage (fertilizer, pesticide, irrigation, water), and economic outcomes (cost, revenue, profit)
Repository Contents
File	Description
Seasonal_Agriculture_Performance_Analysis.ipynb	Complete, pre-executed Jupyter Notebook — data cleaning, EDA, seasonal comparisons, ANOVA significance tests, correlation analysis, and all 10 visualizations
Seasonal_Agriculture_Performance_Analysis.py	Same analysis as a flat Python script
Seasonal_Agriculture_Performance_Analysis.md	Written report covering every stage of the analysis with results tables and interpretation
VOIS_Major_Project_PPT_Filled.pptx	Submission-ready presentation, populated with the project description, methodology and result charts
seasonal_agriculture_performance_dataset.csv	Source dataset (place in the same folder before running)
How to Run
Install dependencies:
bash
   pip install pandas numpy matplotlib seaborn scipy
Place seasonal_agriculture_performance_dataset.csv in the same folder as the notebook/script (rename your CSV to this if it differs).
Run the notebook:
bash
   jupyter notebook Seasonal_Agriculture_Performance_Analysis.ipynb

or run the script directly:

bash
   python Seasonal_Agriculture_Performance_Analysis.py
Methodology
Data cleaning — missing values in Rainfall_mm, Soil_Moisture_pct and Yield_Tonnes_Ha filled using the season-wise median (to preserve seasonal character); outliers (e.g. high sugarcane yield) verified as genuine rather than dropped.
Exploratory analysis — season-wise summary statistics across yield, rainfall, temperature, humidity, cost, revenue, profit and disease/pest risk.
Seasonal comparison — grouped/pivot analysis of yield and profit by season, crop, irrigation method and state.
Statistical testing — one-way ANOVA to test whether yield and profit differences across seasons are statistically significant.
Correlation analysis — correlation of environmental and input variables against yield and profit.
Visualization — bar charts, heatmaps, boxplots and stacked charts built with Matplotlib/Seaborn.
Key Findings
Profit, not yield, is the defining seasonal signal. Yield differs little across seasons (ANOVA p ≈ 0.21, not significant), but profit differs sharply and significantly (ANOVA p < 0.001) — Zaid-season farming is loss-making on average.
Kharif is the strongest season overall (highest rainfall, yield and profit) but also carries the highest disease/pest risk.
Drip irrigation is the most profitable method in every season, and the only one that stays profitable in Zaid.
Every crop peaks in Kharif and troughs in Zaid — a consistent pattern across all 8 crops.
Water usage, not fertilizer or seed quality, is the strongest correlate of yield; fertilizer/pesticide spend shows no meaningful link to profit.
Punjab and Maharashtra are the most profitable states; Andhra Pradesh the least.

See Seasonal_Agriculture_Performance_Analysis.md for full results tables and detailed recommendations.

Tools Used

Python 3 · Pandas · NumPy · Matplotlib · Seaborn · SciPy (stats.f_oneway) · VS Code

Author

Rakshitha
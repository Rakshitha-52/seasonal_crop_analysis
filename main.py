# Seasonal Agriculture Performance Analysis


# 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_style('whitegrid')
plt.rcParams['figure.dpi'] = 100
pd.set_option('display.max_columns', None)

# 2. Load the Dataset

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')
print("Shape:", df.shape)
df.head()

df.info()

df.describe(include='all').T

# 3. Explore Missing Values

df.isnull().sum()[df.isnull().sum() > 0]

#  4. Data Cleaning

for col in ['Rainfall_mm', 'Soil_Moisture_pct', 'Yield_Tonnes_Ha']:
    df[col] = df.groupby('Season')[col].transform(lambda x: x.fillna(x.median()))

# Derived column: profit margin
df['Profit_Margin_pct'] = (df['Profit_INR'] / df['Revenue_INR']) * 100

print("Remaining missing values:", df.isnull().sum().sum())
df.shape



df.sort_values('Yield_Tonnes_Ha', ascending=False)[['Farm_ID','Crop','Season','Yield_Tonnes_Ha']].head(10)

# 5. Categorical Overview

print("States:", df.State.unique())
print("Crops:", df.Crop.unique())
print("Seasons:", df.Season.unique())
print("Irrigation methods:", df.Irrigation_Method.unique())

# 6. Season-wise Summary Statistics

season_summary = df.groupby('Season').agg(
    Count=('Farm_ID', 'count'),
    Avg_Yield=('Yield_Tonnes_Ha', 'mean'),
    Avg_Rainfall=('Rainfall_mm', 'mean'),
    Avg_Temp=('Avg_Temperature_C', 'mean'),
    Avg_Humidity=('Humidity_pct', 'mean'),
    Avg_Fertilizer=('Fertilizer_kg_ha', 'mean'),
    Avg_WaterUsed=('Water_Used_m3', 'mean'),
    Avg_WaterEff=('Water_Efficiency_t_per_1000m3', 'mean'),
    Avg_Cost=('Total_Cost_INR', 'mean'),
    Avg_Revenue=('Revenue_INR', 'mean'),
    Avg_Profit=('Profit_INR', 'mean'),
    Avg_ProfitMargin=('Profit_Margin_pct', 'mean'),
    Avg_DiseaseRisk=('Disease_Pest_Risk_pct', 'mean'),
).round(2)

season_summary

# 7. Yield by Season

season_order = ['Kharif', 'Rabi', 'Zaid']
palette = {'Kharif': '#2e7d32', 'Rabi': '#f9a825', 'Zaid': '#c62828'}

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Season', y='Yield_Tonnes_Ha', order=season_order,
            hue='Season', palette=palette, legend=False, estimator=np.mean, errorbar=None)
plt.title('Average Yield by Season')
plt.ylabel('Yield (Tonnes/Ha)')
plt.tight_layout()
plt.show()

# Statistical significance: does yield differ significantly across seasons?
groups_yield = [df[df.Season == s]['Yield_Tonnes_Ha'].dropna() for s in df.Season.unique()]
f_yield, p_yield = stats.f_oneway(*groups_yield)
print(f"ANOVA — Yield ~ Season: F = {f_yield:.3f}, p = {p_yield:.5f}")
print("Significant at 5%?" , "Yes" if p_yield < 0.05 else "No")

# 8. Profit by Season

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Season', y='Profit_INR', order=season_order,
            hue='Season', palette=palette, legend=False, estimator=np.mean, errorbar=None)
plt.title('Average Profit by Season')
plt.ylabel('Profit (INR)')
plt.tight_layout()
plt.show()

groups_profit = [df[df.Season == s]['Profit_INR'].dropna() for s in df.Season.unique()]
f_profit, p_profit = stats.f_oneway(*groups_profit)
print(f"ANOVA — Profit ~ Season: F = {f_profit:.3f}, p = {p_profit:.5f}")
print("Significant at 5%?", "Yes" if p_profit < 0.05 else "No")

# 9. Environmental Conditions by Season

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, col, title in zip(
    axes,
    ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct'],
    ['Rainfall (mm)', 'Avg Temp (°C)', 'Humidity (%)']
):
    sns.barplot(data=df, x='Season', y=col, order=season_order,
                hue='Season', palette=palette, legend=False, ax=ax, errorbar=None)
    ax.set_title(title)
    ax.set_ylabel('')
plt.tight_layout()
plt.show()

# 10. Irrigation Method Performance by Season

water_eff_pivot = df.pivot_table(index='Irrigation_Method', columns='Season',
                                  values='Water_Efficiency_t_per_1000m3', aggfunc='mean')[season_order]
water_eff_pivot.round(3)

plt.figure(figsize=(6, 4))
sns.heatmap(water_eff_pivot, annot=True, fmt='.2f', cmap='YlGnBu')
plt.title('Water Efficiency (t/1000m³) by Irrigation Method & Season')
plt.tight_layout()
plt.show()

profit_irrigation_pivot = df.pivot_table(index='Irrigation_Method', columns='Season',
                                          values='Profit_INR', aggfunc='mean')[season_order]
profit_irrigation_pivot.round(0)

plt.figure(figsize=(6, 4))
sns.heatmap(profit_irrigation_pivot, annot=True, fmt='.0f', cmap='RdYlGn')
plt.title('Average Profit (INR) by Irrigation Method & Season')
plt.tight_layout()
plt.show()

# Share of irrigation methods used within each season
irrigation_share = pd.crosstab(df.Season, df.Irrigation_Method, normalize='index')[
    ['Drip', 'Sprinkler', 'Flood', 'Rainfed']
].loc[season_order] * 100

irrigation_share.plot(kind='bar', stacked=True, figsize=(6, 4.5), colormap='tab20c')
plt.title('Irrigation Method Share (%) by Season')
plt.ylabel('% of Farms')
plt.legend(title='Irrigation', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()

#  11. Crop-wise Yield Across Seasons

crop_yield_pivot = df.pivot_table(index='Crop', columns='Season',
                                   values='Yield_Tonnes_Ha', aggfunc='mean')[season_order]
crop_yield_pivot.round(2)

crop_yield_no_sugarcane = crop_yield_pivot.drop('Sugarcane')

crop_yield_no_sugarcane.plot(kind='bar', figsize=(7, 4.5),
                              color=[palette[s] for s in season_order])
plt.title('Average Yield by Crop across Seasons (excl. Sugarcane)')
plt.ylabel('Yield (Tonnes/Ha)')
plt.xticks(rotation=30, ha='right')
plt.legend(title='Season')
plt.tight_layout()
plt.show()

# 12. State-wise Profitability

state_profit = df.groupby('State')['Profit_INR'].mean().sort_values(ascending=False)
state_profit.round(0)

plt.figure(figsize=(7, 4.5))
sns.barplot(x=state_profit.values, y=state_profit.index, hue=state_profit.index,
            palette='viridis', legend=False)
plt.title('Average Profit by State')
plt.xlabel('Avg Profit (INR)')
plt.tight_layout()
plt.show()

# 13. Disease / Pest Risk by Season

plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='Season', y='Disease_Pest_Risk_pct', order=season_order,
            hue='Season', palette=palette, legend=False)
plt.title('Disease/Pest Risk (%) Distribution by Season')
plt.tight_layout()
plt.show()

# 14. Correlation Analysis

num_cols = ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day',
            'Soil_pH', 'Soil_Moisture_pct', 'Nitrogen_kg_ha', 'Phosphorus_kg_ha',
            'Potassium_kg_ha', 'Fertilizer_kg_ha', 'Pesticide_Litre_ha',
            'Seed_Quality_Score', 'Water_Used_m3', 'Disease_Pest_Risk_pct', 'Yield_Tonnes_Ha']

corr_with_yield = df[num_cols].corr()['Yield_Tonnes_Ha'].sort_values(ascending=False)
corr_with_yield

key_cols = ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Water_Used_m3',
            'Fertilizer_kg_ha', 'Yield_Tonnes_Ha', 'Profit_INR',
            'Water_Efficiency_t_per_1000m3', 'Disease_Pest_Risk_pct']

plt.figure(figsize=(8, 6))
sns.heatmap(df[key_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('Correlation Heatmap - Key Variables')
plt.tight_layout()
plt.show()


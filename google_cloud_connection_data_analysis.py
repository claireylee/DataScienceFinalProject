# -*- coding: utf-8 -*-
"""Google Cloud Connection/Data Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18B4_VZLdg8PjD6rUr2TDMY-XNkpPgnJE
"""

!pip install google-cloud-bigquery
from google.colab import auth
auth.authenticate_user()
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize BigQuery client
client = bigquery.Client(project="ds-systems-project")  # Project ID
print("Connected to project:", client.project)

# Define the dataset IDs
dataset1_id = "ds-systems-project.major_city_temps"
dataset2_id = "ds-systems-project.state_temps"

# Define table names
major_city_table = f"{dataset1_id}.Global Land Temperatures By Major City"
state_table = f"{dataset2_id}.Global Land Temperatures By State"

# Access and test the first dataset
try:
    dataset1 = client.get_dataset(dataset1_id)
    print(f"Successfully connected to dataset: {dataset1.dataset_id}")
except Exception as e:
    print(f"Error connecting to dataset1 ({dataset1_id}): {e}")

# Access and test the second dataset
try:
    dataset2 = client.get_dataset(dataset2_id)
    print(f"Successfully connected to dataset: {dataset2.dataset_id}")
except Exception as e:
    print(f"Error connecting to dataset2 ({dataset2_id}): {e}")

# Query and fetch data for analysis
major_city_query = f"""
SELECT
    dt,
    averagetemperature,
    averagetemperatureuncertainty,
    city,
    country,
    latitude,
    longitude
FROM
    `{major_city_table}`
WHERE averagetemperature IS NOT NULL
"""

state_query = f"""
SELECT
    dt,
    averagetemperature,
    averagetemperatureuncertainty,
    state,
    country
FROM
    `{state_table}`
WHERE averagetemperature IS NOT NULL
"""

try:
    major_city_temps = client.query(major_city_query).to_dataframe()
    print("======Major City======")
    print(major_city_temps.head())  # Display a sample
    print("Major City Data Description:")
    print(major_city_temps.describe(include='all'))  # Describe major city dataset
except Exception as e:
    print(f"Error fetching data for major cities: {e}")
    major_city_temps = None

try:
    state_temps = client.query(state_query).to_dataframe()
    print("======State======")
    print(state_temps.head())  # Display a sample
    print("State Data Description:")
    print(state_temps.describe(include='all'))  # Describe state dataset
except Exception as e:
    print(f"Error fetching data for states: {e}")
    state_temps = None

# Validate data
if major_city_temps is None or major_city_temps.empty:
    print("Major city data is missing or empty. Exiting.")
    raise ValueError("Major city data is not available for analysis.")
if state_temps is None or state_temps.empty:
    print("State data is missing or empty. Exiting.")
    raise ValueError("State data is not available for analysis.")

# Function to prepare data
def prepare_data(df, region_column):
    df['Year'] = pd.to_datetime(df['dt'], errors='coerce').dt.year
    avg_temp = df.groupby('Year')['averagetemperature'].mean().reset_index()
    avg_temp['Region'] = region_column
    return avg_temp

# Prepare datasets
major_city_avg = prepare_data(major_city_temps, "Major Cities")
state_avg = prepare_data(state_temps, "States")

# Combine datasets for comparison
comparison_data = pd.concat([major_city_avg, state_avg])

# Scatter plot for comparing temperature trends with regression lines
plt.figure(figsize=(12, 6))
sns.scatterplot(data=major_city_avg, x='Year', y='averagetemperature', label='Major Cities', color='blue', alpha=0.6)
sns.regplot(data=major_city_avg, x='Year', y='averagetemperature', scatter=False, color='blue', label='Major Cities Regression Line')
sns.scatterplot(data=state_avg, x='Year', y='averagetemperature', label='States', color='red', alpha=0.6)
sns.regplot(data=state_avg, x='Year', y='averagetemperature', scatter=False, color='red', label='States Regression Line')
plt.title("Temperature Trends: Major Cities vs States (Scatter Plot with Regression Lines)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Temperature (°C)", fontsize=12)
plt.legend(title="Region", fontsize=10)
plt.grid(True)
plt.show()

# KDE plots for temperature distribution
plt.figure(figsize=(10, 6))
sns.kdeplot(data=major_city_avg['averagetemperature'], label='Major Cities', fill=True, color='blue', alpha=0.6)
sns.kdeplot(data=state_avg['averagetemperature'], label='States', fill=True, color='red', alpha=0.6)
plt.title("Temperature Distribution: Major Cities vs States", fontsize=14)
plt.xlabel("Average Temperature (°C)", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.legend(title="Region", fontsize=10)
plt.grid(True)
plt.show()
# Data Science Final Project
Contributors: Claire Lee, Samyu Krishnasamy, Bianca Linares, Semin Ahn

### Data Selection
The datasets came from a Berkeley Earth Surface Temperature Study. These datasets aggregate approximately 1.6 billion temperature records from 16 different archives, spanning centuries from the 18th century to the present. Sourced from Berkeley Earth, it provides detailed temperature data organized by country, state, and city, allowing for granular analysis of global and regional trends. For this project, we specifically used the "Global Land Temperatures by Major City" and "Global Land Temperatures by State" datasets, which include columns such as date, average temperature, temperature uncertainty, and geographic identifiers. The goal of our analysis is to uncover long-term climate trends and regional variations in surface temperatures across major cities and states. We aim to identify global warming patterns by observing changes in average temperatures over time and to compare temperature trends between urban areas (major cities) and broader regions (states) to understand the impact of urbanization and industrialization. Through this analysis, we expect to gain insights into how temperature trends vary geographically, identify urban heat island effects, and highlight regions most vulnerable to climate change.

### ETL Implementation
* Extraction:
  * The datasets, "Global Land Temperatures by Major City" and "Global Land Temperatures by State," were sourced from Kaggle and represent data from the Berkeley Earth Surface Temperature Study.
  * These datasets were retrieved using pandas.read_csv() to load raw data into the pipeline.
* Transformation: Raw datasets were cleaned and prepared for analysis through various steps
  * Normalizing column names: Ensured consistent formatting across datasets
  * Handling missing values: Addressed gaps in the data by cleaning or imputing values
  * Removing duplicates: Prevented redundancy during further processing
  * Structuring data: Reformatted for compatibility with database schema and analytical tools.
* Loading:
  * Initial storage: Transformed datasets were stored in MongoDB. A connection was established for efficient loading and retrieval.
  * Cloud storage: Transformed data was subsequently uploaded to Google Cloud Storage for scalability and accessibility.
  * Analysis-ready format: Final datasets were organized in BigQuery, where table schemas were defined to match the transformed data.
  * Data Storage Considerations:
    * MongoDB: Used for efficient data ingestion and handling bulk operations.
    * Google Cloud Storage: Ensured scalability and secure access for collaborative analysis.
    * BigQuery: Facilitated query optimization and streamlined analytical workflows with schema-defined tables.
* Visualization and Analysis:
  * Various visualization techniques, such as scatter plots and KDE plots, were applied to identify trends, patterns, and outliers in the climate data.

Cloud Storage:

Analysis:

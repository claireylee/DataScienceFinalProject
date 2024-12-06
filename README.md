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
* Loading: MongoDB is used for efficient data ingestion and handling bulk operations.
  * Initial storage: Transformed datasets were stored in MongoDB. A connection was established for efficient loading and retrieval.
* Cloud storage: Ensured scalability and secure access for collaborative analysis
  * Transformed data was subsequently uploaded to Google Cloud Storage for scalability and accessibility.
  * Analysis-ready format: Final datasets were organized in BigQuery, where table schemas were defined to match the transformed data.
  * BigQuery: Facilitated query optimization and streamlined analytical workflows with schema-defined tables.
* Visualization and Analysis:
   * Various visualization techniques, such as scatter plots and KDE plots, were applied to identify trends, patterns, and outliers in the climate data.

### Google Cloud Storage
* Project Creation:
  * Set up a new Google Cloud project to manage resources and permissions effectively.
  * Enabled necessary APIs to support data storage and analysis workflows.
* BigQuery Dataset Setup:
  * Navigated to the BigQuery Console within Google Cloud.
  * Created new datasets to organize and store transformed data efficiently.
* Data Upload:
  * Uploaded the transformed datasets directly to BigQuery tables.
  * Defined table schemas to ensure compatibility with transformed data structure and support for analytical queries.
* Credentials Management and Data Accessibility:
  * Managed credentials to ensure secure access to Google Cloud resources and collaborative functionality.
  * Authorized the connection between Google Colab and Google Cloud to ensure data accessibility for analysis.
  * Ensured data was securely stored within Google Cloud and accessible for analysis while maintaining data security and integrity.

### Analysis
* Temperature Trends Scatterplot:
  * Trend Over Time: Average temperatures have consistently increased over time, highlighting a clear warming trend.
  * Urban vs. Regional: Major cities exhibit higher average temperatures compared to states, emphasizing the urban heat island effect.
  * Key Historical Shifts: A significant rise in average temperatures for both major cities and states is observed around the 1800s, coinciding with key events like urbanization and the Industrial Revolution.
    * Urbanization Impact: Clearing vegetation for housing and infrastructure increased the concentration of heat-absorbing materials like concrete and asphalt.
    * Increased use of fossil fuels (e.g., coal-fired plants and machinery) released heat and pollutants, intensifying the warming trend.
  * Gradual State Trends: While states show a more gradual temperature increase, the long-term trend aligns with global warming patterns.

* Temperature Distribution Histogram:
  * Temperature Distribution:
    * States: State-level temperatures cluster around 10°C, with a broader range of variability.
    * Major Cities: Urban temperatures concentrate around 18°C, indicating a higher average compared to states.
  * Variability:
    * The red curve (states) shows a wider spread, reflecting more significant temperature variations across diverse geographic regions.
    * The blue curve (major cities) is narrower, indicating more consistent temperatures within urban environments.

### Conclusion
* The plots highlight the differences between urban and state-level temperature trends, demonstrating the impact of urbanization and industrialization on climate.
* Key patterns, such as the steady increase in temperatures and the variability between states and cities, provide valuable insights into regional and global climate dynamics.
* These visualizations reinforce the need for targeted strategies to mitigate the effects of climate change, particularly in urban areas.


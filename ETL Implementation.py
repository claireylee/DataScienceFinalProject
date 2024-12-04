from pymongo import UpdateOne
import pandas as pd
from pymongo import MongoClient
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
connection_string = ('mongodb+srv://ngt9dz:Cookies1@cluster1.3osh6.mongodb.net/?retryWrites=true&w=majority&appName'
                     '=Cluster1')
client = MongoClient(connection_string)

# Select database and collection
db = client['finalProject']
csv_files = ['GlobalLandTemperaturesByMajorCity.csv.zip', 'GlobalLandTemperaturesByState.csv.zip']
collection_names = ['major city temperatures', 'state temperatures']


# Transformation: clean and standardize data
def transform_data(dataframe):
    try:
        # Drop missing values
        transformed_df = dataframe.dropna()
        # Standardize column names
        transformed_df.columns = [col.lower().replace(" ", "_") for col in transformed_df.columns]
        logging.info("Data transformed successfully.")
        return transformed_df
    except Exception as e:
        logging.error(f"Error during transformation: {e}")
        return dataframe  # Return original DataFrame in case of failure


# ETL Process with Bulk Insert
for csv_file, collection_name in zip(csv_files, collection_names):
    try:
        # Step 1: Extract
        logging.info(f"Extracting data from {csv_file}...")
        raw_data = pd.read_csv(csv_file)
        logging.info(f"Successfully loaded {csv_file}.")

        # Step 2: Transform
        logging.info(f"Transforming data for {csv_file}...")
        cleaned_data = transform_data(raw_data)

        # Step 3: Load with Bulk Operations
        logging.info(f"Loading data into MongoDB collection '{collection_name}' using bulk operations...")

        collection = db[collection_name]

        bulk_operations = []

        for _, row in cleaned_data.iterrows():
            record = row.to_dict()

            # Assign `_id` explicitly using 'dt' (date)
            if 'dt' in record:
                record['_id'] = record['dt']  # Use 'dt' as the unique identifier

                # Prepare bulk update operation
                bulk_operations.append(
                    UpdateOne(
                        {'_id': record['_id']},  # Find document by _id
                        {'$set': record},  # Update the document if exists, otherwise insert
                        upsert=True
                    )
                )

        # Execute bulk operation
        if bulk_operations:
            result = collection.bulk_write(bulk_operations)
            logging.info(
                f"Bulk write successful: {result.inserted_count} records inserted, {result.modified_count} records updated.")
        else:
            logging.info("No records to process.")

    except Exception as e:
        logging.error(f"Error processing {csv_file}: {e}")

### ELT workflow

1. Data Scrapping:
   We used Selenium and Beautiful Soup for the data scrapping from the Flipkart.

class FlipkartScrapper

- get_top_reviews
- scrape_flipkart_products
- save_to_csv

2. Data Ingestion
   Read the csv files created using Data Scrapping, convert them to LangChain Document.
   I used OpenAI Embedding Model and AstraDB to save the vectors.

class DataIngestion:

- \_load_env_variables
- \_get_csv_path
- \_load_csv
- transform_data
- store_in_vector_db
- run_pipeline

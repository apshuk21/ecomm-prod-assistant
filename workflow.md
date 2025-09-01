## Steps to follow

### Step 1: Create the ETL pipeline

#### Data Extraction

Scrape the data from Amazon/Flipkart. Extract the product details, reviews, metadata, images etc.

#### Data Transformation

In this step we transform the data to the database native format (VectorDB + NoSQL)

#### Data Loading

Load the data to the database

### Step 2: Create the Chatbot

We need to use the GEN-AI capabilities. We can use either classical OR agentic RAG over the data accumaulated in the step 1.

### Code preparation

1. Custom Logger
2. Custom Exception
3. Utils/Config Loader
4. Utils/ Model Loader

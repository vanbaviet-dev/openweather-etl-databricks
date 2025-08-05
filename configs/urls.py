# Base URL for the OpenWeather API
OPENWEATHER_API_BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"

# Base URL for the Datalake Storage (ADLS) Gen2
ADLS_DATA_LAKE_BASE_PATH = "abfss://data@vanbavietdatalake.dfs.core.windows.net/"

# The main container in Azure Data Lake Storage (ADLS) Gen2
ADLS_MAIN_CONTAINER = "data"

# Path of the bronze, silver, and gold layers in the ADLS Gen2
# These paths will be used to store the raw, processed, and aggregated data respectively
BRONZE_LAYER_PATH = f"{ADLS_DATA_LAKE_BASE_PATH}bronze/"
SILVER_LAYER_PATH = f"{ADLS_DATA_LAKE_BASE_PATH}silver/"
GOLD_LAYER_PATH = f"{ADLS_DATA_LAKE_BASE_PATH}gold/"
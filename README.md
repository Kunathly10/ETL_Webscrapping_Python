# Nigeria Universities ETL Project

## Project Summary

The Nigeria Universities ETL (Extract, Transform, Load) project aims to collect, clean, and store information about universities in Nigeria from Wikipedia. The project utilizes web scraping techniques to extract data, applies data transformation processes to clean and structure the information, and finally loads the processed data into a PostgreSQL database.

### Key Features

1. **Data Extraction:**
   - The `extract_data.py` script is responsible for scraping university information from Wikipedia.
   - Utilizes the BeautifulSoup library to parse HTML content and extract relevant data.
   - The extracted data is saved as a CSV file (`newraw_ngn_universities.csv`).

2. **Data Transformation:**
   - The `transform_data.py` script reads the raw CSV file, performs data cleaning and transformation.
   - Columns are selected, null values are handled, and additional features are derived (e.g., fee categories).
   - The transformed data is saved as a new CSV file (`data/transformed_ngn_universities.csv`).

3. **Data Loading:**
   - The `load_to_db.py` script loads the cleaned data into a PostgreSQL database.
   - Utilizes SQLAlchemy to interact with the PostgreSQL database.

### Usage

1. **Installation:**
   - Clone the repository: `git clone https://github.com/your-username/ngn-universities-etl.git`
   - Install dependencies: `pip install -r requirements.txt`
   - Set up PostgreSQL and update `.env` with your database credentials.

2. **Run the ETL Process:**
   - Execute the scripts in the following order:
     - `python extract_data.py`
     - `python transform_data.py`
     - `python load_to_db.py`

### Project Structure

- `extract_data.py`: Web scraping and raw data extraction.
- `transform_data.py`: Data cleaning and transformation.
- `load_to_db.py`: Data loading into PostgreSQL.
- `data/`: Directory containing CSV files for raw and transformed data.

### Dependencies

- pandas
- requests
- beautifulsoup4
- sqlalchemy

### License

This project is licensed under the [MIT License](LICENSE).
‣呅彌敗獢牣灡楰杮⌊攠汴眭瑩⵨敷獢牣灡湩੧‣瑥⵬楷桴眭扥捳慲楰杮�
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from configparser import ConfigParser
config = ConfigParser()
config.read('.env')
db_user_name = config['DB']['db_user_name']
db_password = config['DB']['db_password']
host = config['DB']['host']
port = config['DB']['port']
db_name = config['DB']['db_name']


# Data Extraction layer
def extract_data():
    url = 'https://en.wikipedia.org/wiki/List_of_universities_in_Nigeria'
    scrapped_data = requests.get(url)
    scrapped_data = scrapped_data.content
    soup = BeautifulSoup(scrapped_data, 'lxml') # Parser
    html_data = str(soup.find_all('table'))
    dfs = pd.read_html(html_data)[0:7]
    uni_df = pd.concat(dfs)
    print(uni_df.head)
    uni_df.to_csv('newraw_ngn_universities.csv', index= False)
    print('Data Successfully written to a csv file')

# extract_data()

# Data load transformation layer
def transform_data():
    data = pd.read_csv('newraw_ngn_universities.csv') # Read csv file
    data = data.iloc[:, 0:6]
    data = data.dropna(axis=0)
    def get_fees(value):
        if value == 'State':
            return '350,000'
        elif value == 'Federal':
            return '120,000'
        elif value == 'Private':
            return '850,000'
        else:
            return 'No fees'
    data['Fee'] = data['Funding'].apply(get_fees)
    data = data[['Name', 'State', 'Abbreviation', 'Location', 'Funding', 'Fee']]
    data.to_csv('data/transformed_ngn_universities.csv', index= False)
    print('Data transformed and written to a csv file')

# Data loading layer
def load_to_db():
    data = pd.read_csv('data/transformed_ngn_universities.csv') # Read csv file
    engine = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
    data.to_sql('ngn_universities', con= engine, if_exists='replace', index= False)
    print('Data successfully written to PostgreSQL database')


extract_data()
transform_data()
load_to_db()

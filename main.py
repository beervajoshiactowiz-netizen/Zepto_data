from utils import read_files_zip
from parser import parser
from database import create, insert_into_db
from pprint import pprint
import time
import json

DIR_PATH = r"C:\Users\beerva.joshi\PycharmProjects\AlloTikki\aloo tikki_Adyar_0.html.gz"
TABLE_NAME = 'ItemsData'

def main():
    create(TABLE_NAME)
    raw_data = read_files_zip(DIR_PATH)
    result = parser(raw_data)
    insert_into_db(table_name=TABLE_NAME, data=result)

if __name__ == '__main__':
    st = time.time()
    main()
    tt = time.time() - st
    print(tt)
import gzip
import json
import os

def read_files_zip(path: str):
    try:
        with gzip.open(path,"rt",encoding="utf-8") as f:
            data=json.load(f)
        return data
    except Exception as e:
        print("Error in func:", read_files_zip.__name__, '\nError: ', e)

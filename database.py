import pymysql
from pymysql import connect
import json

def make_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='actowiz',
        database='alootikki_db'
    )
    return conn

def create(table_name: str):
    q = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
    brand                   VARCHAR(255),
    brand_id                VARCHAR(500),
    country_origin          VARCHAR(100),
    description             JSON,
    ingredients             VARCHAR(500),
    manufacturerName        VARCHAR(255),
    item_name               VARCHAR(255),
    variant_id              VARCHAR(500),
    item_pack_size          VARCHAR(500),
    item_image              TEXT,
    item_max_quantity       INTEGER,
    item_mrp                INTEGER,
    item_packsize           INTEGER,
    item_shelflifeinHour    VARCHAR(500),
    unitOfMeasure           VARCHAR(50),
    item_id                 VARCHAR(500),
    rating                  JSON,
    item_type               VARCHAR(100),
    discounted_sellingprice INTEGER,
    discount_amount         INTEGER,
    category                VARCHAR(255)
);
    """
    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    conn.close()

def fetch():
    pass

def insert_into_db(table_name: str, data: list):

    Values = []
    for item in data:
        item['rating'] = json.dumps(item.get('rating') or {})
        item['description'] = json.dumps(item.get('description') or {})
        Values.append(tuple(item.values()))

    # build query from first item's keys
    cols = ", ".join(data[0].keys())
    placeholders = ", ".join(['%s'] * len(data[0].keys()))
    q = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    conn = make_connection()
    cursor = conn.cursor()
    cursor.executemany(q, Values)
    conn.commit()


if __name__ == '__main__':
    pass
import requests as req
import json
import psycopg2


def get_data():
    response_data = req.get("https://softwium.com/api/books")
    json_data = json.loads(response_data.content)

    columns = json_data[0].keys()
    res = []
    for ele in json_data:
        res.append([ele.get(c) for c in columns])

    return res, columns


def push_data_to_rds(data, columns):
    try:

        db_conn = psycopg2.connect(
            database="postgres",
            user='postgres',
            password='postgres',
            host='hostname',
            port='5432'
        )
        cursor = db_conn.cursor()
        col_str = ",".join(columns)
        # we need to create table prior to this program execution
        for each_row in data:
            cursor.execute(f"INSERT into books({col_str}) VALUES (%s, %s,%s,%s,%s)", each_row)

        db_conn.commit()
        db_conn.close()
    except Exception as e:
        print(e)
        print("Exception while performing database operations ")


if __name__ == "__main__":
    data, cols = get_data()
    push_data_to_rds(data, cols)

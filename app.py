import json
import os
import psycopg2
from flask import Flask
from flask import render_template
import re

app = Flask(__name__)
PROJECTS_COLUMNLIST = ['image', 'thumbnail', 'name', 'summary', 'id', 'description']
PROJECTS_TABLE = 'projects'

SOCIALLINKS_COLUMNLIST = ['icon', 'type', 'url']
SOCIALLINKS_TABLE = 'sociallinks'


def connect_to_db():
    conn = None
    data_url = os.getenv("DATABASE_URL")
    config_list = re.split(':|/|@', data_url)[3:]

    try:
        conn = psycopg2.connect(
            host=config_list[2],
            database=config_list[4],
            user=config_list[0],
            password=config_list[1],
            port=config_list[3])

    except Exception as error:
        print("DATABASE CONNECTION FAILED" + str(error))
    finally:
        return conn


def query_data_base(db, statement):
    rows = []
    try:
        if db is not None:
            cur = db.cursor()
            cur.execute(statement)
            rows = cur.fetchall()
            cur.close()
    except Exception as error:
        print("QUERY TO DATABASE FAILED" + str(error))
    finally:
        if db is not None:
            db.close()
    return rows


def build_query(column_list, table):
    column = ','.join([str(col) for col in column_list])

    statement = "SELECT" + ' ' + column + ' ' + "FROM" + ' ' + table

    return statement


def select_query(column_list, table):
    statement = build_query(column_list, table)
    db = connect_to_db()
    rows = query_data_base(db, statement)
    return select_query_result_to_dictionary(column_list, rows)


def select_query_result_to_dictionary(columns, rows):
    dic_list = []
    for index, row in enumerate(rows):
        dic = {}
        for i, column in enumerate(columns):
            dic[column] = rows[index][i]
        dic_list.append(dic)

    return dic_list


@app.route("/")
def index():
    social_media_list = select_query(SOCIALLINKS_COLUMNLIST, SOCIALLINKS_TABLE)
    projects_list = select_query(PROJECTS_COLUMNLIST, PROJECTS_TABLE)

    with open("db.json", "r") as f:
        data = json.loads(f.read())

    return render_template('index.html', social_media_list=social_media_list, data=data, projects_list=projects_list,
                           projectslen=len(projects_list),
                           socialmedialen=len(social_media_list))


@app.route("/privacy-policy")
def privacy():
    social_media_list = select_query(SOCIALLINKS_COLUMNLIST, SOCIALLINKS_TABLE)
    projects_list = select_query(PROJECTS_COLUMNLIST, PROJECTS_TABLE)

    with open("db.json", "r") as f:
        data = json.loads(f.read())

    return render_template('privacy-policy.html', social_media_list=social_media_list, data=data,
                           projects_list=projects_list,
                           projectslen=len(projects_list),
                           socialmedialen=len(social_media_list))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

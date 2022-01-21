import json
import os
import psycopg2
from flask import Flask
from flask import render_template
import re

app = Flask(__name__)

QUERY_SOCIAL_MEDIA_ICONS = "SELECT icon,type,url FROM sociallinks"


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


def select_query(statement):
    db = connect_to_db()
    rows = query_data_base(db, statement)
    return rows


@app.route("/")
def index():
    social_media_list = select_query(QUERY_SOCIAL_MEDIA_ICONS)

    with open("db.json", "r") as f:
        data = json.loads(f.read())

    projects = data["projects"]

    return render_template('index.html', social_media_list=social_media_list, data=data, projectslen=len(projects),
                           socialmedialen=len(social_media_list))


@app.route("/privacy-policy")
def privacy():
    social_media_list = select_query(QUERY_SOCIAL_MEDIA_ICONS)

    with open("db.json", "r") as f:
        data = json.loads(f.read())

    projects = data["projects"]

    return render_template('privacy-policy.html', social_media_list=social_media_list, data=data,
                           projectslen=len(projects),
                           socialmedialen=len(social_media_list))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

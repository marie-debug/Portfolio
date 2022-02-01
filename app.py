import json
import os
from flask import Flask
from flask import render_template

from database import DataBase

app = Flask(__name__)
PROJECTS_COLUMNLIST = ['image', 'thumbnail', 'name', 'summary', 'id', 'description']
PROJECTS_TABLE = 'projects'

SOCIALLINKS_COLUMNLIST = ['icon', 'type', 'url']
SOCIALLINKS_TABLE = 'sociallinks'

data_url = os.getenv("DATABASE_URL")

db = DataBase(data_url)


@app.route("/")
def index():
    social_media_list = db.select_query(SOCIALLINKS_COLUMNLIST, SOCIALLINKS_TABLE)
    projects_list = db.select_query(PROJECTS_COLUMNLIST, PROJECTS_TABLE)

    with open("db.json", "r") as f:
        data = json.loads(f.read())

        pages = data["pages"]

        print(pages)

    return render_template('index.html', social_media_list=social_media_list, data=data, pages=pages,
                           projects_list=projects_list, pageslen=len(pages),
                           projectslen=len(projects_list),
                           socialmedialen=len(social_media_list))


@app.route("/<url>")
def privacy(url):
    url = '/' + url

    social_media_list = db.select_query(SOCIALLINKS_COLUMNLIST, SOCIALLINKS_TABLE)
    projects_list = db.select_query(PROJECTS_COLUMNLIST, PROJECTS_TABLE)

    with open("db.json", "r") as f:
        data = json.loads(f.read())

        pages = data["pages"]

        page = get_page(pages, url)

    if page == None:
        return render_template('404.html', pages=pages, social_media_list=social_media_list, data=data,
                               projects_list=projects_list, pageslen=len(pages),
                               projectslen=len(projects_list),
                               socialmedialen=len(social_media_list))

    return render_template('page.html', page=page, pages=pages, social_media_list=social_media_list, data=data,
                           projects_list=projects_list, pageslen=len(pages),
                           projectslen=len(projects_list),
                           socialmedialen=len(social_media_list))


def get_page(pages, url):
    for page in pages:
        if page["isSection"] == False:
            if page["url"] == url:
                return page
    return None


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

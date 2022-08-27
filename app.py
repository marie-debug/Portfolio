import json
import os
from flask import Flask
from flask import render_template

from database import DataBase

app = Flask(__name__)
PROJECTS_COLUMNLIST = ['image', 'thumbnail', 'name', 'summary', 'id', 'description', 'image_alt_text', 'published']
PROJECTS_TABLE = 'projects'

SOCIALLINKS_COLUMNLIST = ['icon', 'type', 'url', 'link_alt_text']
SOCIALLINKS_TABLE = 'sociallinks'

PAGES_COLUMLIST = ['is_section', 'url', 'title', 'content', 'name']
PAGES_TABLE = 'pages'

data_url = os.getenv("DATABASE_URL")

db = DataBase(data_url)


@app.route("/")
def index():
    social_media_list = db.select_query(SOCIALLINKS_COLUMNLIST, SOCIALLINKS_TABLE)
    projects_list = db.select_query(PROJECTS_COLUMNLIST, PROJECTS_TABLE)
    pages_list = db.select_query(PAGES_COLUMLIST, PAGES_TABLE)

    return render_template('index.html', social_media_list=social_media_list, pages=pages_list,
                           projects_list=projects_list, pageslen=len(pages_list),
                           projectslen=len(projects_list),
                           socialmedialen=len(social_media_list))


@app.route("/<url>")
def page(url):
    url = '/' + url

    social_media_list = db.select_query(SOCIALLINKS_COLUMNLIST, SOCIALLINKS_TABLE)
    projects_list = db.select_query(PROJECTS_COLUMNLIST, PROJECTS_TABLE)
    pages_list = db.select_query(PAGES_COLUMLIST, PAGES_TABLE)

    page = get_page(pages_list, url)

    if page == None:
        return render_template('404.html', pages=pages_list, social_media_list=social_media_list,
                               projects_list=projects_list, pageslen=len(pages_list),
                               projectslen=len(projects_list),
                               socialmedialen=len(social_media_list))

    return render_template('page.html', page=page, pages=pages_list, social_media_list=social_media_list,
                           projects_list=projects_list, pageslen=len(pages_list),
                           projectslen=len(projects_list),
                           socialmedialen=len(social_media_list))


@app.route("/resume")
def resume():
    social_media_list = db.select_query(SOCIALLINKS_COLUMNLIST, SOCIALLINKS_TABLE)
    projects_list = db.select_query(PROJECTS_COLUMNLIST, PROJECTS_TABLE)
    pages_list = db.select_query(PAGES_COLUMLIST, PAGES_TABLE)


    return render_template('resume.html', pages=pages_list, social_media_list=social_media_list,
                           projects_list=projects_list, pageslen=len(pages_list),
                           projectslen=len(projects_list),
                           socialmedialen=len(social_media_list))


def get_page(pages, url):
    for page in pages:
        if page["is_section"] == False:
            if page["url"] == url:
                return page
    return None


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

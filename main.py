import json
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    with open("db.json", "r") as f:
        data = json.loads(f.read())

    projects = data["projects"]

    socialmedia = data["socialmedia"]

    return render_template('index.html', data=data, projectslen=len(projects), socialmedialen=len(socialmedia))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

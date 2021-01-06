import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.url_for('index', extra_param=[])

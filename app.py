import flask
from werkzeug import secure_filename
from .data import pages

app = flask.Flask(__name__)


@app.route('/')
def home():
    return 'Its working, use a page URL'


@app.route('/<page>')
def page(page):
    page_fname = '{}.html'.format(secure_filename(page))
    data = getattr(pages, page)
    return flask.render_template('layout.html', page_fname=page_fname, data=data)


@app.route('/css/<path:filename>')
def css(filename):
    return flask.send_from_directory('cpm-public/css', filename)


@app.route('/js/<path:filename>')
def js(filename):
    return flask.send_from_directory('cpm-public/js', filename)

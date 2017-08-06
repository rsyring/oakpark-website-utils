import flask
from werkzeug import secure_filename
from .data import pages

app = flask.Flask(__name__)


@app.route('/')
def home():
    return 'Its working, use a page URL'


@app.route('/<page>.html')
def page(page):
    source = flask.request.args.get('source', None)
    page_fname = '{}.html'.format(secure_filename(page))
    data = getattr(pages, page, None)
    if source is not None:
        template = flask.render_template(page_fname, data=data)
        response = flask.make_response(template)
        response.headers['Content-Type'] = 'text/plain'
        return response
    return flask.render_template('layout.html', page_fname=page_fname, data=data, page=page.title())


@app.route('/css/<path:filename>')
def css(filename):
    return flask.send_from_directory('cpm-public/css', filename)


@app.route('/js/<path:filename>')
def js(filename):
    return flask.send_from_directory('cpm-public/js', filename)

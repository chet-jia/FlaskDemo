from flask import Flask
from jinja2.utils import generate_lorem_ipsum


app = Flask(__name__)


@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return '''
        <h1>A very long post </h1>
        <div class='body'>%s</div>
        <button id="load">Load More</button>
    '''
from flask import *

app = Flask(__name__)

app.secret_key("HI")

app.route('/')
def index():
    return render_template('index.html')

app.route('/profile')
def profile():
    return render_template('login')
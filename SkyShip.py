from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/who')
def who():
    return 'Whoweare Page'

@app.route('/Product')
def product():
    return 'Product Page'

@app.route('/Demo')
def demo():
    return 'Demo Page'

@app.route('/Demo/Dashboard')
def dashboard():
    return 'Dashboard page'

@app.route('/Demo/Dashboard/Manage')
def manage():
    return 'Manage Page'

@app.route('/Demo/Dashboard/Manage/Detail')
def detail():
    return  'Detail Page'

if __name__ == '__main__':
    app.debug = True
    app.run()

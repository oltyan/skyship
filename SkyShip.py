from flask import Flask, render_template, redirect, url_for, request, session
import cgi, sys,cgitb; cgitb.enable()
import wtforms

app = Flask(__name__)
app.secret_key = "my session"

@app.route('/')
def index():
    return render_template("Index.html")

@app.route('/about')
def about():
    return render_template("About.html")

@app.route('/who')
def who():
    return render_template("whoweare.html")

@app.route('/product')
def product():
    return render_template("product.html")

@app.route('/calculator',methods=['GET', 'POST'])
def calculator():
    form = cgi.FieldStorage()
    if(form.getvalue('Infrastructure') is None):
        infrastructure = 10000
    else:
        infrastructure = float(form.getvalue('Infrastructure'))
    if(form.getvalue('timetoprovision')is None):
        timetoprovision = 30
    else:
        timetoprovision = float(form.getvalue('timetoprovision'))
    if(form.getvalue('provisionhours') is None):
        provisionhours = 20
    else:
        provisionhours = float(form.getvalue('provisionhours'))
    if(form.getvalue('devtime') is None):
        devtime = 30
    else:
        devtime = float(form.getvalue('devtime'))
    list = [infrastructure,timetoprovision,provisionhours,devtime]
    total = ((list[0]*0.30)/2)+((list[1]*14*8)/2)+(list[2]*0.20*62.50)+(list[3]*62.50)

    return render_template("Calculator.html")


if __name__ == '__main__':
    app.debug = True
    app.run()

from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static\images"
currentdirectory = os.path.dirname(os.path.abspath(__file__))


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/login', methods=('GET', 'POST'))
def home():
    return render_template('home.html')


@app.route('/agriculturist', methods=('GET', 'POST'))
def agriculturist():
    return render_template('agriculturist.html')


@app.route('/farmers', methods=('GET', 'POST'))
def farmers():
    return render_template('farmers.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/pricemonitoring')
def pricemonitoring():
    return render_template('pricemonitoring.html')

@app.route('/landarea')
def landarea():
    return render_template('landarea.html')



@app.route('/organic-agriculture')
def pdf():
    return render_template('materials.html')
@app.route('/avian-influenza')
def pdf1():
    return render_template('materials1.html')
@app.route('/hog-production')
def pdf2():
    return render_template('materials2.html')
@app.route('/palay')
def pdf3():
    return render_template('materials3.html')
@app.route('/urbangardening')
def pdf4():
    return render_template('materials4.html')
@app.route('/pdf5')
def pdf5():
    return render_template('materials5.html')
@app.route('/pdf6')
def pdf6():
    return render_template('materials6.html')
@app.route('/pdf7')
def pdf7():
    return render_template('materials7.html')
@app.route('/pdf8')
def pdf8():
    return render_template('materials8.html')
@app.route('/pdf9')
def pdf9():
    return render_template('materials9.html')
@app.route('/pdf10')
def pdf10():
    return render_template('materials10.html')
@app.route('/pdf11')
def pdf11():
    return render_template('materials11.html')
@app.route('/pdf12')
def pdf12():
    return render_template('materials12.html')
@app.route('/pdf13')
def pdf13():
    return render_template('materials13.html')
if __name__ == '__main__':
    app.run()

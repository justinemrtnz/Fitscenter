from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER']="static\images"
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

@app.route('/upnews', methods=('GET', 'POST'))
def upnews():
    if request.method == 'POST':

        caption = request.form['caption']
        pic = request.files['upload_img']
        if pic.filename!="":
            filepath=os.path.join(app.config['UPLOAD_FOLDER'],pic.filename)
            pic.save(filepath)
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (caption, content) VALUES (?, ?)',
                         (caption, pic.filename))
            conn.commit()
            conn.close()
            return redirect(url_for('home'))

    return render_template('create.html')


if __name__ == '__main__':
    app.run()

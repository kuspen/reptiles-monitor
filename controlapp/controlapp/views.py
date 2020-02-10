from flask import request, redirect, url_for, render_template, flash, session
from controlapp import app, client

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('entries/index.html')
    elif request.method == 'POST':
        if request.form['action'] == "capture":
            client.connect()
            client.get_img_data()
        
        return render_template('entries/index.html')

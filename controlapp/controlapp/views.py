import os
from flask import request, redirect, url_for, render_template, flash, session
from controlapp import app, client

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('entries/index.html')
    elif request.method == 'POST':
        if request.form['action'] == "capture":
            client.connect()
            image_name = client.get_img_data()
            print(os.getcwd())
            return render_template('entries/index.html', cap_img='static/cap_images/' + image_name)
        else:
            return render_template('entries/index.html')


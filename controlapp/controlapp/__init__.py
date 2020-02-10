from flask import Flask
import sys
import monitorapp.src.clientapp.reptilesclient

app = Flask(__name__)
app.config.from_object(__name__)

client = monitorapp.src.clientapp.reptilesclient.ReptilesClient() 

import controlapp.views

from controlapp import app
import monitorapp.src.clientapp.reptilesclient

app.run(host='127.0.0.1', port=5000, debug=True)
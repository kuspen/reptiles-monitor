from controlapp import app

@app.route('/')
def index():
    print('index')
    return 'Hello World!'

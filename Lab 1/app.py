from flask import Flask
app = Flask(__name__)
@app.route('/')
def index ():
    return "Hello World!"
#comment
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    # handle login logic
    else:
    # show login form
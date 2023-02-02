from flask import make_response

@app.route('/')
def index():
    response = make_response('Hello World!')
    response.headers['Content-Type'] = 'text/plain'
    return response

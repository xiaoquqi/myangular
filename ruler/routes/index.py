from ruler import app
from flask_security import auth_token_required, http_auth_required
from flask import jsonify

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/dummy-api/', methods=['GET'])
#@http_auth_required
@auth_token_required
def dummyAPI():
    ret_dict = {
        "Key1": "Value1",
        "Key2": "value2"
    }
    return jsonify(items=ret_dict)

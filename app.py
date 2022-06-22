import os
import json
from flask_migrate import Migrate
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db) 

from models import Client
from get_zip_data import get_zip_dataset

zip_dataset = get_zip_dataset()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/create_user', methods=['POST'])
def create():
    request_data = request.get_json()
    first_name = request_data['first_name']
    middle_name = request_data['middle_name']
    last_name = request_data['last_name']
    email = request_data['email']
    zipcode = request_data['zipcode']

    info = {
        'first_name': first_name,
        'middle_name': middle_name,
        'last_name': last_name,
        'email': email,
        'zipcode': zipcode,
    }

    zip_data = zip_dataset.get(zipcode, None)
    if zip_data is not None:
        info['city'] = zip_data['place']
        info['country'] = zip_data['country']
        info['state'] = zip_data['state']

    try:
        client = Client(**info)
        db.session.add(client)
        db.session.commit()

        response = app.response_class(
            response=json.dumps(info),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        return e.__class__

if __name__ == '__main__':
    app.run()

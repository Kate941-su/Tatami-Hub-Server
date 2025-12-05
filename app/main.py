from flask import Flask, jsonify
# If using Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from mock.mock_items import get_mock_items

app = Flask(__name__)

# Configure the database connection string
# 'db' here refers to the name of the PostgreSQL service in docker-compose.yml

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# Define a simple model (optional, but good practice)

# class Item(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)

#     def __repr__(self):
#         return f'<Item {self.name}>'

@app.route('/')
def home():
    return "Welcome to the Dockerized Flask API!"

@app.route('/api/items', methods=['GET'])
def list_items():
    # Example database query (requires initial table creation/migration)
    # items = Item.query.all()
    # return jsonify([{'id': item.id, 'name': item.name} for item in items])
    result = get_mock_items()
    return jsonify(result)


if __name__ == '__main__':
    # When running with Docker, the host should be 0.0.0.0
    app.run(host='0.0.0.0', port=8000)
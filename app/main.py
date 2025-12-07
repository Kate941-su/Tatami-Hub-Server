from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from typing import Optional
from mock.mock_items import get_mock_items

app = Flask(__name__)

# Configure the database connection string
# 'db' here refers to the name of the PostgreSQL service in docker-compose.yml
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    
    # 1. Primary Key and Required Fields
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80), nullable=False)
    user_id: int = db.Column(db.Integer, nullable=False)
    title: str = db.Column(db.String(80), nullable=False)
    
    # 2. Boolean Flags (Correctly defined)
    n_good: bool = db.Column(db.Boolean, nullable=False) 
    n_bad: bool = db.Column(db.Boolean, nullable=False)
    
    # 3. List/Complex Field (Using JSON or Text)
    # Using JSON is ideal for PostgreSQL to store lists of strings
    tags: list[str] = db.Column(db.JSON, nullable=False, default=[]) 

    # 4. URL/Optional Fields (Using String/Text with explicit nullability)
    link_url: str = db.Column(db.String(255), nullable=True) 
    thumbnail_url: str = db.Column(db.String(255), nullable=True) 
    description: Optional[str] = db.Column(db.Text, nullable=True)
    embedded_url: Optional[str] = db.Column(db.String(255), nullable=True)\

    def __repr__(self):
        return f'<Item {self.name}>'

with app.app_context():
   db.create_all()

@app.route('/test')
def test():
    return make_response(jsonify({'message': 'test route'}), 200)

@app.route('/api/items', methods=['GET'])
def get_mock_all():
    # Example database query (requires initial table creation/migration)
    # items = Item.query.all()
    # return jsonify([{'id': item.id, 'name': item.name} for item in items])
    result = get_mock_items()
    return make_response(jsonify(result), 200)

@app.route('/api/items/<int:page>', methods=['GET'])
def get_item_by_page(page):
    return f"アイテム ID: {id} (型: {type(page)})"

@app.route('/api/items/<int:id>', methods=['GET'])
def get_item_by_int(id):
    return f"アイテム ID: {id} (型: {type(id)})"

# @app.route('/api/item/', methods=['POST'])
# def post_item():
#   try:
#     data = request.get_json()
#     new_user = User(username=data['username'], email=data['email'])
#     db.session.add(new_user)
#     db.session.commit()
#     return make_response(jsonify({'message': 'user created'}), 201)
#   except e:
#     return make_response(jsonify({'message': 'error creating user'})),

if __name__ == '__main__':
    # When running with Docker, the host should be 0.0.0.0
    app.run(host='0.0.0.0', port=8080)
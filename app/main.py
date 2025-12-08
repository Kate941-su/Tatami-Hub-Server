from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from typing import Optional
from mock.mock_items import get_mock_items
from model.item import ItemModel

app = Flask(__name__)

# ---- Flask configurations ---- 

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
    embedded_url: Optional[str] = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Item {self.name}>'

with app.app_context():
    db.create_all()

# ---- End configurations ---- 

@app.route('/test')
def test():
    return make_response(jsonify({'message': 'test route'}), 200)

@app.route('/api/mock/items', methods=['GET'])
def get_mock_all():
    # Example database query (requires initial table creation/migration)
    # items = Item.query.all()
    # return jsonify([{'id': item.id, 'name': item.name} for item in items])
    result = get_mock_items()
    return make_response(jsonify(result), 200)

@app.route('/api/items', methods=['GET'])
def get_all():
    items = db.session.execute(db.select(Item)).scalars().all() 
    response_items = [ItemModel(
            id = item.id,
            datetime_string = item.datetime_string),
            user_id = item.user_id,
            n_good = 0,
            n_bad = 0,
            title = item.title,
            tags = item.tags,
            link_url =  item.link_url,
            thumbnail_url =  item.thumbnail_url,
            description =  'Description.',
            embedded_url  =  None,
        ) for item in items]
    return make_response(jsonify(response_items), 200)


@app.route('/api/items/<int:page>', methods=['GET'])
def get_item_by_page(page):
    return f"アイテム ID: {id} (型: {type(page)})"

@app.route('/api/items/<int:id>', methods=['GET'])
def get_item_by_int(id):
    return f"アイテム ID: {id} (型: {type(id)})"

@app.route('/api/post/item', methods=['POST'])
def post_item():
    try:
        itemModel = ItemModel.fromJson(request.get_json())
        item = Item(
            # The database will automatically generate the ID
            name = itemModel.title,
            user_id = itemModel.user_id, 
            title = itemModel.title,
            n_good = 0,
            n_bad = 0,
            tags = itemModel.tags, # Saved as JSON in PostgreSQL            
            # Optional fields
            link_url = itemModel.link_url,
            thumbnail_url = itemModel.thumbnail_url,
            description = itemModel.description,
            embedded_url = None # Or provide a URL string
        )
    
    except Exception as e: 
        print(f"Error processing JSON: {e}")
        return make_response(jsonify({'error_code': '1', 'message': str(e)}), 400)

    db.session.add(item)
    
    try:
        db.session.commit()
        print(f"Successfully added Item: {itemModel.title} with ID: {itemModel.id}")
        return make_response("", 200)
    
    except Exception as e:
        db.session.rollback()
        print(f"Error adding item to database: {e}")
        return make_response(jsonify({'error_code': '2', 'message': str(e)}), 400)

if __name__ == '__main__':
    # When running with Docker, the host should be 0.0.0.0
    app.run(host='0.0.0.0', port=8080)
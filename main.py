from flask import Flask
from flask_sqlalchemy import SQLAlchemy # ORM

app = Flask(__name__)

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'

db = SQLAlchemy(app)

# Create Model
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'destination': self.destination,
            'country': self.country,
            'rating': self.rating

        }
    
with app.app_context():
    db.create_all()   


# Create Routes
@app.route('/')
def home():
    return 'Hello World'










if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify
from models import db, Food, User, BMIRecord

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db.init_app(app)

@app.route('/foods', methods=['GET'])
def get_foods():
    foods = Food.query.all()
    return jsonify([food.serialize for food in foods])

@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')
    bmi = weight / (height ** 2)
    return jsonify({'bmi': bmi})

@app.route('/chat', methods=['POST'])
def chat():
    # Mock chat response
    message = request.get_json().get('message')
    return jsonify({'response': f"You said: {message}"})

if __name__ == '__main__':
    app.run()

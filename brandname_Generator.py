from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    city_name = data.get('city', '').strip()
    pet_name = data.get('pet', '').strip()
    
    if not city_name or not pet_name:
        return jsonify({'error': 'City and pet names are required'}), 400
    
    suggestions = [
        city_name + " " + pet_name,
        pet_name + " " + city_name,
        "The " + city_name + " " + pet_name,
        city_name + "'s " + pet_name,
        pet_name + " from " + city_name,
        "The " + pet_name + " of " + city_name
    ]
    
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
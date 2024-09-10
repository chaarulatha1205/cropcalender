from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def generate_ai_response(crop_name):
    crop_name = crop_name.lower()

    climate = random.choice(["Tropical", "Subtropical", "Temperate", "Mediterranean", "Arid"])
    temperature_low = random.randint(10, 25)
    temperature_high = temperature_low + random.randint(5, 15)
    soil_types = ["Loamy", "Sandy", "Clay", "Silt", "Peat", "Chalky"]
    soil_characteristics = ["well-draining", "nutrient-rich", "acidic", "alkaline", "fertile"]
    
    if any(char in 'aeiou' for char in crop_name):
        climate = "Tropical" if climate == "Arid" else climate
    if len(crop_name) > 6:
        soil_types = soil_types[:3]
    
    soil_type = f"{random.choice(soil_types)}, {random.choice(soil_characteristics)}"
    
    growing_methods = [
        f"Start from seeds in {random.choice(['early spring', 'late summer', 'mid-autumn'])}",
        f"Transplant seedlings when they reach {random.randint(2, 8)} inches tall",
        f"Direct sow in {random.choice(['rows', 'mounds', 'scattered patterns'])}",
        f"Propagate from cuttings in a {random.choice(['greenhouse', 'cold frame', 'indoor nursery'])}",
        f"Plant bulbs or tubers {random.randint(4, 8)} inches deep"
    ]
    growing_method = random.choice(growing_methods)
    
    return {
        "name": crop_name.capitalize(),
        "climate": climate,
        "temperature": f"{temperature_low}°C to {temperature_high}°C ({temperature_low*9//5+32}°F to {temperature_high*9//5+32}°F)",
        "soil_type": soil_type,
        "growing_method": growing_method
    }

@app.route('/crop-details', methods=['POST'])
def get_crop_details():
    app.logger.info(f"Received request: {request.method} {request.url}")
    app.logger.info(f"Request headers: {request.headers}")
    app.logger.info(f"Request body: {request.data}")

    data = request.json
    app.logger.info(f"Parsed JSON data: {data}")

    crop_name = data.get('name') if data else None
    
    if not crop_name:
        app.logger.warning("No crop name provided")
        return jsonify({"error": "No crop name provided"}), 400

    crop_data = generate_ai_response(crop_name)
    app.logger.info(f"Generated response: {crop_data}")
    return jsonify(crop_data)

if __name__ == '__main__':
    app.run(debug=True)
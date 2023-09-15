from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to your MongoDB server (change the connection URI as needed)
client = MongoClient('mongodb://localhost:27017')
db = client['animals_db']  # Replace 'your_database_name' with your database name

# Sample initial list of animals as dictionaries
animals = [{'name': 'Cat', 'description': 'A small domesticated carnivorous mammal.', 'url': 'https://en.wikipedia.org/wiki/Cat'},
           {'name': 'Dog', 'description': 'A domesticated mammal known for loyalty and companionship.', 'url': 'https://en.wikipedia.org/wiki/Dog'},
           {'name': 'Elephant', 'description': 'A large herbivorous mammal with a trunk.', 'url': 'https://en.wikipedia.org/wiki/Elephant'}]

@app.route('/')
def index():
    # Retrieve the list of animals from MongoDB
    animals_from_db = list(db.animals.find())
    return render_template('index.html', animals=animals_from_db)

@app.route('/add_animal', methods=['POST'])
def add_animal():
    new_animal_name = request.form.get('new_animal')
    new_animal_description = request.form.get('new_description')
    new_animal_url = request.form.get('new_url')
    if new_animal_name and new_animal_description and new_animal_url:
        new_animal = {'name': new_animal_name, 'description': new_animal_description, 'url': new_animal_url}
        # Insert the new animal into MongoDB
        db.animals.insert_one(new_animal)

    # Retrieve the updated list of animals from MongoDB
    animals_from_db = list(db.animals.find())
    return jsonify({'animals': animals_from_db})

@app.route('/remove_animal', methods=['POST'])
def remove_animal():
    animal_name_to_remove = request.form.get('animal')
    # Remove the animal from MongoDB
    db.animals.delete_one({'name': animal_name_to_remove})

    # Retrieve the updated list of animals from MongoDB
    animals_from_db = list(db.animals.find())
    return jsonify({'animals': animals_from_db})

if __name__ == '__main__':
    app.run(port=3001)


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample initial list of animals as dictionaries
animals = [{'name': 'Cat', 'description': 'A small domesticated carnivorous mammal.', 'url': 'https://en.wikipedia.org/wiki/Cat'},
           {'name': 'Dog', 'description': 'A domesticated mammal known for loyalty and companionship.', 'url': 'https://en.wikipedia.org/wiki/Dog'},
           {'name': 'Elephant', 'description': 'A large herbivorous mammal with a trunk.', 'url': 'https://en.wikipedia.org/wiki/Elephant'}]

@app.route('/')
def index():
    return render_template('index.html', animals=animals)

@app.route('/add_animal', methods=['POST'])
def add_animal():
    new_animal_name = request.form.get('new_animal')
    new_animal_description = request.form.get('new_description')
    new_animal_url = request.form.get('new_url')
    if new_animal_name and new_animal_description and new_animal_url:
        new_animal = {'name': new_animal_name, 'description': new_animal_description, 'url': new_animal_url}
        animals.append(new_animal)
    return jsonify({'animals': animals})

@app.route('/remove_animal', methods=['POST'])
def remove_animal():
    animal_name_to_remove = request.form.get('animal')
    for animal in animals:
        if animal['name'] == animal_name_to_remove:
            animals.remove(animal)
            break
    return jsonify({'animals': animals})

if __name__ == '__main__':
    app.run(port=3002)

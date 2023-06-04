from flask import Flask, jsonify
import csv

app = Flask(__name__)

def read_data():
    data = {}
    with open('data/capital_data.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        for row in reader:
            # Convert country to lowercase
            data[row[0].lower()] = row[1]
    return data

@app.route('/')
def index():
    data = read_data()
    return jsonify(data)

@app.route('/<country>')
def country(country):
    data = read_data()
    # Convert country to lowercase
    capital = data.get(country.lower(), "Country not found")
    return jsonify({country: capital})

if __name__ == '__main__':
    app.run(debug=True)

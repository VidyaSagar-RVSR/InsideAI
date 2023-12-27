from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load dataset (created from preprocess.py) from the JSON file
dataset_file_path = '/Users/vidyasagar/Desktop/IMBD_FLASK/dataset.json'
with open(dataset_file_path, 'r') as json_file:
    dataset = json.load(json_file)

# Function to check if the input text is in the dataset
def check_input(input_text):
    for category, values in dataset.items():
        if input_text in values:
            return f"{input_text} is a {category}"
    return "Data not found"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_text = request.form['input_text']
        result = check_input(input_text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

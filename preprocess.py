#Necessary libraries
import pandas as pd
import re
import spacy
import json

# Path to the CSV file on Google Drive
file_path = '//Users/vidyasagar/Downloads/IMDB Dataset.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
df.head()

# Select the top 5000 records
top_5k_df = df.head(5000)

# Function to remove special characters and hyperlinks
def clean_text(text):
    # Remove special characters
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    # Remove hyperlinks
    text = re.sub(r'http\S+', '', text)
    return text

# Apply the cleaning function to the 'review' column
top_5k_df['cleaned_review'] = top_5k_df['review'].apply(clean_text)

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to extract entities (user names and cities)
def extract_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'GPE']:
            entities.append((ent.text, ent.label_))
    return entities

# Apply the entity extraction function to the 'cleaned_review' column
top_5k_df['entities'] = top_5k_df['cleaned_review'].apply(extract_entities)

# Function to determine entity type
def get_entity_type(entity):
    name, label = entity
    if label == 'PERSON':
        return 'Person'
    elif label == 'GPE':
        return 'City'
    else:
        return 'Other'

# Add the 'Entity' column based on the extracted entities
top_5k_df['Entity'] = top_5k_df['entities'].apply(lambda x: [get_entity_type(entity) for entity in x])

# Display the DataFrame with the new columns
top_5k_df.head()



# Assuming top_5k_df is the DataFrame you have
# Extract names and places from the 'entities' column
names = []
places = []

for entities_list in top_5k_df['entities']:
    for entity, label in entities_list:
        if label == 'PERSON':
            names.append(entity)
        elif label == 'GPE':
            places.append(entity)

# Create a dictionary with 'name' and 'place' entities
json_dataset = {
    "name": names,
    "place": places
}

# Convert the dictionary to a JSON string
json_string = json.dumps(json_dataset, indent=2)

print(json_string)

# Specify the file path where you want to save the JSON file
json_file_path = '/Users/vidyasagar/Desktop/IMBD_FLASK/dataset.json'

# Write the JSON string to the file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_string)

print(f"JSON file saved successfully at: {json_file_path}")
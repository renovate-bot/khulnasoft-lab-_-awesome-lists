import os
import json

def process_data():
    raw_data_dir = 'data/raw/'
    processed_data_dir = 'data/processed/'

    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)

    for filename in os.listdir(raw_data_dir):
        if filename.endswith('.json'):
            with open(os.path.join(raw_data_dir, filename), 'r') as file:
                data = json.load(file)

            # Example of processing: filtering repositories with more than 1000 stars
            processed_data = [repo for repo in data if repo.get('stars', 0) > 1000]

            with open(os.path.join(processed_data_dir, filename), 'w') as file:
                json.dump(processed_data, file, indent=4)

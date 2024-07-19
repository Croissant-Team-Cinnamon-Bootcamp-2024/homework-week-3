import json 

dataset_file_path = "data/image_paths.json"
with open(dataset_file_path, 'r') as file:
    data = json.load(file)
import kagglehub
import os
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("claudiodavi/superhero-set")

print("Path to dataset files:", path)

for file in os.listdir(path):
    print(file)
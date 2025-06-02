import os
import sys
from sentence_transformers import SentenceTransformer

os.makedirs("./models", exist_ok=True)
model_path = './models/all-MiniLM-L6-v2'

if os.path.exists(model_path):
    print("Model already exists at:", model_path)
    sys.exit(0)

try:
    print("Downloading sentence transformer model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    model.save(model_path)
    print("Model downloaded and saved successfully!")
except Exception as e:
    print("Error downloading model:", str(e))

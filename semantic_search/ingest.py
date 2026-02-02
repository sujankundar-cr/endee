import sys
import os

# Add Endee src directory to Python path
sys.path.append(os.path.abspath("../src"))

from sentence_transformers import SentenceTransformer
from endee.client import Client

model = SentenceTransformer("all-MiniLM-L6-v2")
client = Client()

with open("data/docs.txt", "r") as f:
    documents = f.readlines()

embeddings = model.encode(documents)

client.insert(
    vectors=embeddings.tolist(),
    metadata=[{"text": doc.strip()} for doc in documents]
)

print("✅ Documents successfully stored in Endee")

import sys
import os

# Add Endee src directory to Python path
sys.path.append(os.path.abspath("../src"))

from sentence_transformers import SentenceTransformer
from endee.client import Client

model = SentenceTransformer("all-MiniLM-L6-v2")
client = Client()

query = input("Enter search query: ")
query_embedding = model.encode([query])

results = client.search(query_embedding.tolist(), top_k=3)

print("\n🔍 Top Results:")
for r in results:
    print("-", r["metadata"]["text"])

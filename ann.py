from sentence_transformers import SentenceTransformer
from faqs import FAQData
import numpy as np
import faiss

# Step 1: Load model and prepare FAQ data
model = SentenceTransformer('all-MiniLM-L6-v2')

faq_data = FAQData()
faqs = faq_data.faqs
questions = faq_data.get_questions()

# Convert FAQs to embeddings (vectors)
faq_embeddings = model.encode(questions, convert_to_numpy=True)

# Step 2: Build a FAISS Index (IVF for ANN)
dimension = faq_embeddings.shape[1]  # 384
n_clusters = 3  # small number for demo

quantizer = faiss.IndexFlatL2(dimension)  # base index for clustering
index = faiss.IndexIVFFlat(quantizer, dimension, n_clusters, faiss.METRIC_L2)

# Train the index with the FAQs
index.train(faq_embeddings)  # needed for IVF indices
index.add(faq_embeddings)

# Step 3: Encode a new query
query = "How do I import API credentials in bulk?"
query_embedding = model.encode([query], convert_to_numpy=True)

# Step 4: Perform approximate nearest neighbor search
k = 1  # number of nearest neighbors to return
distances, indices = index.search(query_embedding, k)

# Step 5: Apply threshold logic
L2_THRESHOLD = 0.75  # empirically chosen; tweak as needed
matched_index = indices[0][0]
matched_distance = distances[0][0]

if matched_distance <= L2_THRESHOLD:
    print(f"Match found: \"{questions[matched_index]}\" (Distance: {matched_distance:.4f})")
else:
    print(f"No close match. Closest was: \"{questions[matched_index]}\" (Distance: {matched_distance:.4f})")

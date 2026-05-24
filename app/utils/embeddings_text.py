from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

text1 = "AI improves healthcare"
text2 = "Machine Learning helps medicine"
text3 = "Football match tonight"


emb1 = model.encode(text1, convert_to_numpy=True)
emb2 = model.encode(text2, convert_to_numpy=True)
emb3 = model.encode(text3, convert_to_numpy=True)

sim1 = cosine_similarity(emb1.reshape(1, -1), emb2.reshape(1, -1))
sim3 = cosine_similarity(emb1.reshape(1, -1), emb3.reshape(1, -1))



print("Healthcare Similarity:", sim1)

print("Football Similarity:", sim3)

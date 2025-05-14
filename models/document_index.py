import faiss
import numpy as np
from models.embeddings import get_embedding

class DocumentIndex:
    def __init__(self):
        self.dimension = 768
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add_document(self, text):
        embedding = get_embedding(text)
        self.index.add(np.array([embedding], dtype=np.float32))
        self.texts.append(text)

    def search(self, query, top_k=3):
        if len(self.texts) == 0:
            return ["Aucun document trouvé dans la base de données."]

        query = normalize_query(query)
        query_embedding = get_embedding(query)
        distances, indices = self.index.search(np.array([query_embedding], dtype=np.float32), top_k)

        print(f"🔍 Recherche FAISS - Indices: {indices}, Distances: {distances}")

        # Vérifier si FAISS renvoie des indices valides
        valid_results = [self.texts[i] for i in indices[0] if i < len(self.texts)]
        if not valid_results:
            return ["Je n'ai trouvé aucun document pertinent pour cette requête."]
        
        return valid_results

    def save_index(self, path):
        faiss.write_index(self.index, path)

    def load_index(self, path):
        self.index = faiss.read_index(path)
        
    def normalize_query(query):
        query = query.replace(" XP ", " Xeroderma Pigmentosum ")
        query = query.replace("XP", "Xeroderma Pigmentosum")  # au cas où sans espaces
        return query

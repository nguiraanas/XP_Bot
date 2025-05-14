from sentence_transformers import CrossEncoder

# Charger le cross-encoder une seule fois
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(question, candidate_texts, top_k=3):
    pairs = [(question, passage) for passage in candidate_texts]
    scores = reranker.predict(pairs)

    # Classement décroissant des passages selon leur pertinence
    sorted_passages = [x for _, x in sorted(zip(scores, candidate_texts), reverse=True)]
    return sorted_passages[:top_k]

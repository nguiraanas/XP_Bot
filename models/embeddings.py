from sentence_transformers import SentenceTransformer

model = SentenceTransformer("pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb")

def get_embedding(text):
    return model.encode(text)

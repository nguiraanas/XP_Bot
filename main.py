# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models.document_indexer import DocumentIndexer
from models.embeddings import generate_embeddings
from models.reranker import rerank_documents
from utils.pdf_extractor import extract_text_from_pdf

import faiss
import pickle

app = FastAPI()

# Configurer les templates et les fichiers statiques
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Charger l'index FAISS
index = faiss.read_index("data/faiss_index.bin")
with open("data/index_mapping.pkl", "rb") as f:
    mapping = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/query", response_class=HTMLResponse)
async def query(request: Request):
    form_data = await request.form()
    user_query = form_data.get("query")

    # Embedding de la requête
    query_embedding = generate_embeddings(user_query)

    # Recherche dans l'index
    D, I = index.search(query_embedding.reshape(1, -1), k=5)
    retrieved_docs = [mapping[i] for i in I[0]]

    # Re-ranking
    reranked_docs = rerank_documents(user_query, retrieved_docs)

    return templates.TemplateResponse("index.html", {"request": request, "docs": reranked_docs})

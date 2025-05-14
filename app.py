from flask import Flask, render_template, request, jsonify
import ollama
import os
from utils.pdf_extractor import extract_text_from_pdf
from models.document_index import DocumentIndex
from models.reranker import rerank


app = Flask(__name__)

# Initialisation de FAISS et chargement des documents
doc_index = DocumentIndex()

pdf_folder = "pdfs/"
index_path = "data/faiss_index.bin"

if os.path.exists(index_path):  
    doc_index.load_index(index_path)
    print(f"🔄 Index FAISS chargé avec {len(doc_index.texts)} documents.")
else:
    print("📂 Chargement et indexation des PDF...")
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            text = extract_text_from_pdf(os.path.join(pdf_folder, file))
            print(f"📄 {file} - {len(text)} caractères extraits")
            doc_index.add_document(text)

    doc_index.save_index(index_path)
    print(f"✅ Index FAISS créé avec {len(doc_index.texts)} documents.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    
    # Étape 1 : recherche sémantique (BioBERT + FAISS)
    candidate_texts = doc_index.search(user_message, top_k=10)
    
    # Étape 2 : re-ranking (Cross-Encoder)
    top_chunks = rerank(user_message, candidate_texts, top_k=3)
    
    # Étape 3 : création du prompt pour Mistral
    context = "\n\n".join(top_chunks)
    prompt = (
            "You are an intelligent assistant. Use the following information if relevant, "
            "but feel free to supplement your response with your own knowledge if necessary.\n\n"
            f"Available information:\n{context}\n\n"
            f"Question: {user_message}\n\n"
            "If the provided information is insufficient, rely on your own knowledge. "
            "Always respond in English."
    )

    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    
    return jsonify({"response": response['message']['content']})


if __name__ == "__main__":
    app.run(debug=True)

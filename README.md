# 🧠 XP_Bot – Chatbot IA pour les enfants de la lune (RAG)

XP_Bot est un assistant intelligent basé sur la technique **RAG (Retrieval-Augmented Generation)**. Il aide les familles, les médecins et les aidants à obtenir des réponses fiables à partir de documents médicaux concernant la maladie **Xeroderma Pigmentosum (XP)**.

---

## 🎯 Objectif

Fournir une plateforme interactive et personnalisée capable de :
- Répondre à des questions sur le XP à partir de sources médicales fiables
- Vulgariser les termes médicaux pour une meilleure compréhension
- Rendre l'information accessible, même dans des zones mal desservies

---

## 🛠️ Fonctionnalités

- 🔎 **Recherche sémantique** avec embeddings et FAISS
- 📄 **Extraction automatique** de texte depuis des fichiers PDF
- 💬 **Génération de réponses contextuelles** via des modèles LLM
- 🌐 **Interface web** simple avec Flask
- 🧠 Architecture modulaire pour une extension facile

---

## 🗂️ Structure du projet

XP_Bot/
├── app.py # Serveur Flask
├── main.py # Logique principale du chatbot
├── models/
│ ├── document_index.py # Indexation des documents
│ ├── embeddings.py # Génération d'embeddings
│ └── reranker.py # (Optionnel) Reranker pour améliorer les résultats
├── utils/
│ └── pdf_extractor.py # Extraction du texte à partir de PDF
├── data/
│ └── faiss_index.bin # Index vectoriel FAISS
├── static/
│ ├── script.js # JavaScript pour l'interface
│ └── style.css # Style CSS
├── templates/
│ └── index.html # Interface utilisateur
├── questions.txt # Exemples de questions
├── test.py # Tests unitaires ou d’intégration
├── test_extraction.py # Test de l’extraction PDF
├── .gitignore # Fichiers à ignorer
└── README.md # Ce fichier

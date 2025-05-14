from flask import Flask, render_template, request, jsonify
import ollama
import os
from utils.pdf_extractor import extract_text_from_pdf
from models.document_index import DocumentIndex

pdf_folder = "pdfs/"
print(os.listdir(pdf_folder))

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        text = extract_text_from_pdf(os.path.join(pdf_folder, file))
        print(f"📄 {file} - {len(text)} caractères extraits")
        
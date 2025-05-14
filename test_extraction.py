import os
from utils.pdf_extractor import extract_text_from_pdf

pdf_folder = "pdfs"

if not os.path.exists(pdf_folder):
    print("❌ Dossier 'pdfs' introuvable. Ajoutez vos PDF avant d'exécuter ce script.")
    exit()

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        text = extract_text_from_pdf(os.path.join(pdf_folder, file))
        print(f"📄 {file} - {len(text)} caractères extraits")
        print("🔍 Aperçu du contenu :")
        print(text[:500])  # Afficher les 500 premiers caractères
        print("=" * 80)

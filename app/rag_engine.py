from app.gcloud_utils import download_file_from_gcs
from app.ollama_interface import query_llm
import os
def query_without_rag(question, temperature):
    
    # Pose une question au LLM sans utiliser le contexte.
    
    return query_llm(question, temperature)

def query_with_rag(question, temperature, cloud_file_name):
   
    local_file_path = "downloaded_context.txt"

    try:
        # Télécharge le fichier depuis Google Cloud Storage
        download_file_from_gcs(cloud_file_name, local_file_path)

        # Vérifier la taille du fichier (éviter les contextes trop longs)
        max_file_size = 5 * 1024 * 1024  
        if os.path.getsize(local_file_path) > max_file_size:
            return "Erreur : Le fichier est trop volumineux pour être utilisé comme contexte."

        # Charger le contenu du fichier
        with open(local_file_path, "r", encoding="utf-8", errors="replace") as f:
            context = f.read()

        # Limite le contexte à une taille raisonnable pour le modèle
        max_context_length = 2000  # Limite à 2000 caractères
        if len(context) > max_context_length:
            context = context[:max_context_length] + "\n... (contenu tronqué)"

        # Construit le prompt pour le LLM
        prompt = f"Voici un contexte à considérer :\n{context}\n\nQuestion : {question}"
        return query_llm(prompt, temperature)

    except FileNotFoundError:
        return "Erreur : Le fichier spécifié n'a pas pu être téléchargé."
    except UnicodeDecodeError:
        return "Erreur : Le fichier contient des caractères non valides."
    except Exception as e:
        return f"Erreur inattendue : {str(e)}"

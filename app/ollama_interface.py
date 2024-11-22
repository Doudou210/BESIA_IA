
import requests
import json  # Pour gérer les réponses JSON

def query_llm(prompt, temperature):
    """
    Interroge le modèle LLM en mode streaming et assemble la réponse.
    """
    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": "llama3.2",  # Modèle utilisé
        "prompt": prompt,
        "temperature": temperature
    }


    try:
        # Lancer une requête POST en mode streaming
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()

        full_response = ""  # Pour assembler les fragments de réponse
        for line in response.iter_lines():
            if line:
                try:
                    # Charger chaque ligne comme JSON
                    partial_response = json.loads(line)
                    # Ajouter le texte à la réponse complète
                    full_response += partial_response.get("response", "")
                except ValueError as ve:
                    print(f"Erreur de parsing JSON pour la ligne : {line.decode('utf-8')}")
                    print(f"Détails de l'erreur : {ve}")

        # Retourner la réponse complète ou un message par défaut
        return full_response.strip() if full_response.strip() else "Aucune réponse générée par le modèle."
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la requête : {e}"
    except ValueError:
        return "Erreur : Impossible de traiter la réponse du serveur."

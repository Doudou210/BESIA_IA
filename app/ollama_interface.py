
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


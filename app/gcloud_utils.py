from google.cloud import storage

BUCKET_NAME = "besia"  # Remplace par le nom de ton bucket

def upload_file_to_gcs(file, file_name):
    """
    Upload un fichier vers Google Cloud Storage.
    :param file: Le fichier à uploader (objet de type Stream)
    :param file_name: Nom du fichier tel qu'il sera sauvegardé sur le bucket
    """
    storage_client = storage.Client.from_service_account_json("gcloud_config.json")
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file_name)

    # Uploader le fichier
    blob.upload_from_file(file)
    return f"https://storage.googleapis.com/{BUCKET_NAME}/{file_name}"

def download_file_from_gcs(file_name, destination_file_path):
    """
    Télécharge un fichier depuis Google Cloud Storage.
    :param file_name: Nom du fichier dans le bucket
    :param destination_file_path: Chemin local pour sauvegarder le fichier téléchargé
    """
    storage_client = storage.Client.from_service_account_json("gcloud_config.json")
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file_name)

    # Téléchargement du fichier
    blob.download_to_filename(destination_file_path)
    return destination_file_path

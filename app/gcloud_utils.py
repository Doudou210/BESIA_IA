from google.cloud import storage

BUCKET_NAME = "besia"  # Remplace par le nom de ton bucket

def upload_file_to_gcs(file, file_name):
   
    storage_client = storage.Client.from_service_account_json("gcloud_config.json")
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file_name)

    # Uploader le fichier
    blob.upload_from_file(file)
    return f"https://storage.googleapis.com/{BUCKET_NAME}/{file_name}"

def download_file_from_gcs(file_name, destination_file_path):
   
    storage_client = storage.Client.from_service_account_json("gcloud_config.json")
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file_name)

    # Téléchargement du fichier
    blob.download_to_filename(destination_file_path)
    return destination_file_path

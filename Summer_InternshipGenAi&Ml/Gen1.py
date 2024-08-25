from googleapiclient.discovery import build
from google.oauth2 import service_account

def search_google_drive(query):
    # Set up the credentials
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    # Replace with the actual path to your service account JSON file
    SERVICE_ACCOUNT_FILE = '/path/to/your/service_account.json'  
    
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Build the Drive API client
    service = build('drive', 'v3', credentials=credentials)
    
    # Search for files
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(f"{item['name']} ({item['id']})")

# Example usage
search_google_drive("name contains 'report'")
import sys
import json
import os

# Mi Version que sirve 

sys.path.insert(0, "path/to/gpapi.zip")  # Replace with the actual path to the zip file

from dotenv import load_dotenv
from gpapi.googleplay import GooglePlayAPI

try:
    # Initialize the API
    api = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="bacon")
    print(f"GOOGLE API: {api}")
except Exception as e:
    print(f"Error initializing API: {e}")
    sys.exit(1)

try:
    # Login to the API
    # Load environment variables from .env file
    load_dotenv()

    email = os.getenv("EMAIL_ACCOUNT")
    password = os.getenv("APP_PASSWORD")

    if not email or not password:
        print("Error: Email or password not found in .env file")
        sys.exit(1)
    api.login(email=email, password=password)
except Exception as e:
    print(f"Error logging in: {e}")
    sys.exit(1)

try:
    # Search for an app
    search = str(input("Enter the package name of the app (e.g., com.example.app): "))
    if not search.startswith("com."):
        print("Error: Please enter a valid package name starting with 'com.'")
        sys.exit(1)

    results = api.search(search)
    
    # Download the APK
    apk_data = api.download(search)
    download_folder = "downloads"
    os.makedirs(download_folder, exist_ok=True)

    apk_file_path = os.path.join(download_folder, f"{search.split('.')[-1]}.apk")
    with open(apk_file_path, "wb") as apk_file:
        for chunk in apk_data['file']['data']:
            apk_file.write(chunk)
    print(f"APK downloaded to '{apk_file_path}'")

    # Export results to a file
    with open("search_results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)
    print("Results exported to 'search_results.json'")
except Exception as e:
    print(f"Error searching for app: {e}")

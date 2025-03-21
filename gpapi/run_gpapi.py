import sys
import json

sys.path.insert(0, "path/to/gpapi.zip")  # Replace with the actual path to the zip file

from gpapi.googleplay import GooglePlayAPI
from dotenv import load_dotenv
import os

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
    search = str(input("Search for an app - APP NAME: "))
    results = api.search(search)
    # results = api.search("pinterest")
    print("Search Results:", results)

    # Export results to a file
    with open("search_results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)
    print("Results exported to 'search_results.json'")
except Exception as e:
    print(f"Error searching for app: {e}")
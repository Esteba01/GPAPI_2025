import sys
sys.path.insert(0, "path/to/gpapi.zip")  # Replace with the actual path to the zip file

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
    email = "obsec.epn@gmail.com"
    password = "obsecepn2024"
    api.login(email=email, password=password)
except Exception as e:
    print(f"Error logging in: {e}")
    sys.exit(1)

try:
    # Search for an app
    results = api.search("example app")
    print("Search Results:", results)
except Exception as e:
    print(f"Error searching for app: {e}")
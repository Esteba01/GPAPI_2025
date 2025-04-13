import sys
import json
import os
from datetime import datetime

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
    
    # Extract and save privacy policy URL
    if results and isinstance(results, list) and len(results) > 0:
        if 'doc' in results[0] and 'details' in results[0]['doc']:
            privacy_url = results[0]['doc']['details'].get('privacyPolicyUrl')
            # Initialize privacy info string
            privacy_info = []
            
            if privacy_url:
                privacy_info.append(f"Privacy Policy URL: {privacy_url}")
            else:
                privacy_info.append("Warning: No privacy policy URL found for this app")
            
            # Check for additional privacy-related fields
            if 'appDetails' in results[0]['doc']['details']:
                app_details = results[0]['doc']['details']['appDetails']
                if 'containsAds' in app_details:
                    privacy_info.append(f"Contains Ads: {'Yes' if app_details['containsAds'] else 'No'}")
                if 'dataSafety' in app_details:
                    privacy_info.append(f"Data Safety: {app_details['dataSafety']}")
            
            # Print all privacy info
            print("\n".join(privacy_info))
            
            # Save privacy policy info to file
            os.makedirs("privacy_policies", exist_ok=True)
            policy_content = f"Privacy Information for {search}\n" + "\n".join(privacy_info) + f"\nLast checked: {datetime.now().strftime('%Y-%m-%d')}"
            policy_file = os.path.join("privacy_policies", f"privacy_info_{search}.txt")
            with open(policy_file, "w", encoding="utf-8") as f:
                f.write(policy_content)
            print(f"Privacy information saved to '{policy_file}'")
except Exception as e:
    print(f"Error searching for app: {e}")

from gpapi.googleplay import GooglePlayAPI

# Initialize the API
api = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="bacon")

# Login to the API
email = "your_email@gmail.com"
password = "your_password"
api.login(email=email, password=password)

# Search for an app
results = api.search("example app")
print("Search Results:", results)

# Get app details
details = api.details("com.example.app")
print("App Details:", details)
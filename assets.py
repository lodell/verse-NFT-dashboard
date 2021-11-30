# Import requests package to make http requests
import requests, json

# Create dictionary containing API request information
# First filter by collection - need to retrieve collection slug for the value
# "limit" limits the number of assets retrieved from a collection or other specified class
# We can create separate json files for each request, e.g. each asset or collection etc.

params = {
    'collection': 'the-wanderers',
    'limit': 1
}

# Create an object that holds to OpenSea API
# Set filters for get request in dictionary and include in http API request
API = requests.get("https://api.opensea.io/api/v1/assets", params=params)


# We can view available data in json format - add to file for analysis
# Without further filters the request will pull all data from the-wanderers collection

#print(API.json())
print(json.dumps(API.json()))
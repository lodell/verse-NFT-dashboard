import requests, json
import math, time

url = "https://api.opensea.io/api/v1/assets"

headers = {
    "X-API-KEY": "48dd67bd8fa5479b9e3ee431fe617904",
    "Accept": "application/json"
}

offset = 0

data = {'assets': []}

# fetch assets in collection 50 at a time
while True:
    params = {
        'collection': 'azuki',
        'offset': offset,
        'limit': 50
    }
 
    #r = requests.get('https://api.opensea.io/api/v1/assets', headers=headers, params=params)
    r = requests.request("GET", url, headers=headers, params=params)
    
    response = r.json()

    try:
        (response['assets'])
    except KeyError:
        print("offset throws null assets @", offset)
        print(response)
        time.sleep(3)
        r = requests.request("GET", url, headers=headers, params=params)
        response = r.json()
       


    #print(json.dumps(response['assets']))
    data['assets'].extend(response['assets'])


    if len(response['assets']) < 50:
        break
    
    offset += 50

    # uncomment if you want to add a delay in case you get throttled
    #time.sleep(1)

# dump entire data structure, you can redirect this output to a file
#print(json.dumps(data))

with open('the-wanderers.json', 'w') as outfile:
    json.dump(data, outfile)

listings = []
buy_now_listings = 0
for asset in data['assets']:
    if asset["sell_orders"] is not None:
         sell_order = asset["sell_orders"][0]
         
         if sell_order["sale_kind"] == 0:
            tokenID = asset['token_id']
            currency_sym = sell_order["payment_token_contract"]["symbol"]
            currency_decimals = sell_order["payment_token_contract"]["decimals"]
            price = float(sell_order["current_price"]) / math.pow(10, currency_decimals)
            listings.append([asset['token_id'], price])
            buy_now_listings+=1
        
print(buy_now_listings)
#print(len(listings['assets']))
 #           st.write(f"Buy Now: {price} {currency_sym}")

with open('the-wanderers_listings.json', 'w') as outfile:
    json.dump(listings, outfile)
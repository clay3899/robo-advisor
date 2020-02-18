# app/robo_advisor.py

import requests
import json
import dotenv
import datetime

request_url ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)

#print(type(response))
#print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text)


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()


#quit()

symbol = "0"
symbol_list =[]
while symbol != "done":
    
    symbol = input("Please enter the stock symbols of your choice. When done, type 'done': ")
    
    if float(len(symbol)) <= 5 and symbol.isalpha():
        symbol_list.append(symbol)
        pass
    else:
        print("Error: Please enter a valid stock symbol")
        pass    
        
    
    
    
    pass    

symbol_list.remove("done")


print("-------------------------")
print("SELECTED SYMBOLS: ", symbol_list)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: ", last_refreshed)
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
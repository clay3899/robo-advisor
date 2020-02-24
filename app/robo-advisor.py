# app/robo_advisor.py
import csv
import json
from datetime import datetime
import os

import requests
from dotenv import load_dotenv


load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


now = datetime.now()
request_time = now.strftime("%Y/%m/%d %H:%M:%S")
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

counter = 0
symbol_list =[]
symbol = "0"
while symbol != "done":


    symbol = input("Please enter the stock symbols of your choice. When done, type 'done': ")

    if float(len(symbol)) <= 5 and symbol.isalpha() and counter <= 5:
            symbol_list.append(symbol)
            counter = counter + 1
            pass
    elif counter > 5:
            print("Error: System can only compute 5 stocks")
            pass
    else:
            print("Error: Please enter a valid stock symbol")
            pass    
                
    pass

symbol_list.remove("done")

for s in symbol_list:
    
    request_url =f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={s}&apikey={api_key}"
    response = requests.get(request_url)
    #breakpoint()
    
    if "Error Message" in response.text:
        print("ERROR: YOU ENTERED AN INVALID SYMBOL.")
        exit()
        pass
    else:
        parsed_response = json.loads(response.text)
        tsd = parsed_response["Time Series (Daily)"]
        pass

    
    dates = list(tsd.keys()) #TODO : sort to make sure the data is chronological


    latest_day = dates[0]
    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    latest_close = tsd[latest_day]["4. close"]


    #get the high price from each day
    high_prices = []
    low_prices = []
    for d in dates:
        high_price = tsd[d]["2. high"]
        high_prices.append(float(high_price))

        #low prices now
        low_price = tsd[d]["3. low"]
        low_prices.append(float(low_price))
        pass

    #maximum of all the high prices
    recent_high = max(high_prices)

    #minimum of all the low prices
    recent_low = min(low_prices)
    #breakpoint()


    #quit()




    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"{s}.csv")


    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above

        #looping to write row
        for d in dates:
            daily_prices = tsd[d]
            writer.writerow({
                "timestamp": d,
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"],
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                "volume":daily_prices["5. volume"],
                })
            pass




    print("-------------------------")
    print("SELECTED SYMBOL: ", s)
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("REQUEST AT: ", request_time)
    print("-------------------------")
    print("LATEST DAY: ", last_refreshed)
    print("LATEST CLOSE: ", to_usd(float(latest_close)))
    print("RECENT HIGH: ", to_usd(float(recent_high)))
    print("RECENT LOW: ", to_usd(float(recent_low)))
    print("-------------------------")
    
    
    threshold = .08
    decision = "unsure"
    reason = "IDK"


    if float(latest_close) == float(recent_low):
        decision = "BUY"
        reason = "NEVER SELL LOW. UNLESS THE COMPANY IS BURNING TO THE GROUND."
        pass
    elif float(latest_close) >= (float(recent_high) - (float(recent_high) * threshold)):
        decision = "HOLD or SELL"
        reason = "NEVER BUY HIGH. UNLESS YOU ARE FROM THE FUTURE AND KNOW IT WILL CONTINUE RISING."
        pass
    elif float(latest_close) <= (float(recent_low) + (float(recent_low) * threshold)):
        decision = "BUY"
        reason = "STOCK MAY RECOVER. RECENT TRENDS SHOW THE STOCK IS IN RECOVERY"
        pass
    else:
        decision = "BUY"
        reason = "I WANT MY COMMISSION. LOGIC SYSTEMS CANNOT COMPUTE."
        pass



    print("RECOMMENDATION: ", decision)
    print("RECOMMENDATION REASON: ", reason)
    print("-------------------------")
    print("WRITING DATA TO CSV: ", csv_file_path)
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")


    






    pass

       




#csv_file_path = "data/prices.csv" # a relative filepath


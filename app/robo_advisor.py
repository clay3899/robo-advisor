# app/robo_advisor.py
import csv
import json
from datetime import datetime
import os

import requests
from dotenv import load_dotenv


load_dotenv()

def to_usd(my_price):
    #converts a paramater to a formatted string of  $ USD
    return "${0:,.2f}".format(my_price)


def compile_url(symbol, API):
    url =f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API}"
    return url

def get_response(url):
    
    #i mplements the request function to access the date
    
    requesting = requests.get(url)
    return requesting

def parse_response(responses):
    # parses the response to make data readable
    parsed = json.loads(responses.text)
    return parsed

def transform_parsed(parsed_responses):
    # parsed_respose should be a dictionary representing the original json response
    # it should have keys: Meta Data and time Series Daily
    tsd = parsed_responses["Time Series (Daily)"]
    rows = []

    for date, daily_prices in tsd.items():
        row = {
        "timestamp": date,
        "open": float(daily_prices["1. open"]),
        "high": float(daily_prices["2. high"]),
        "low": float(daily_prices["3. low"]),
        "close": float(daily_prices["4. close"]),
        "volume": int(daily_prices["5. volume"])
    }
        rows.append(row)
        pass
    return rows


def write_to_csv(rows, csv_filepath):
    # write to csv file using parameters of file path and rows see above
    # rows is a list of dictionaries
    # csv_filepath should be a string

    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for row in rows:
            writer.writerow(row)
    return True



if __name__ == "__main__":
    now = datetime.now()
    request_time = now.strftime("%Y/%m/%d %H:%M:%S")
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", default ="OOPS")

    if api_key == "OOPS":
        print("Please put an API key in the .env file you created called ALPHAVANTAGE_API_KEY")
        exit()
        pass

    

    print("WELCOME TO THE ROBO ADVISOR")

    print("HERE WE'LL TELL YOU WHAT STOCKS TO BUY OR SELL")

    print("GET READY TO MAKE MONEY!")




    symbol_list =[]
    symbol = "0"
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

    if len(symbol_list) >= 5:
        print("Error: System can only compute 5 stocks")
        exit()
        pass

    for s in symbol_list:

        request_url = compile_url(s, api_key)
        response = get_response(request_url)
        
        #breakpoint()

        if "Error Message" in response.text:
            print("ERROR: YOU ENTERED AN INVALID SYMBOL.")
            exit()
            pass
        else:
            parsed_response = parse_response(response)
            last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
            rows = transform_parsed(parsed_response)
            pass

        
        
        
                #get the high price from each day


        high_prices = []
        low_prices = []

        latest_close = rows[0]["close"]
        high_prices = [row["high"] for row in rows]
        low_prices = [row["low"] for row in rows]

        recent_high = max
        

        #maximum of all the high prices
        recent_high = max(high_prices)

        #minimum of all the low prices
        recent_low = min(low_prices)
        #breakpoint()


        #quit()




        csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"{s}.csv")


        write_to_csv(rows, csv_file_path)


        divider = "-------------------------"

        print(divider)
        print("SELECTED SYMBOL: ", s)
        print(divider)
        print("REQUESTING STOCK MARKET DATA...")
        print("REQUEST AT: ", request_time)
        print(divider)
        print("LATEST DAY: ", last_refreshed)
        print("LATEST CLOSE: ", to_usd(float(latest_close)))
        print("RECENT HIGH: ", to_usd(float(recent_high)))
        print("RECENT LOW: ", to_usd(float(recent_low)))
        print(divider)


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
        print(divider)
        print("WRITING DATA TO CSV: ", csv_file_path)
        print(divider)
        print("HAPPY INVESTING!")
        print(divider)









        pass






    #csv_file_path = "data/prices.csv" # a relative filepath


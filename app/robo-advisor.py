# app/robo_advisor.py

symbol = "0"
symbol_list =[]
while symbol != "done":
    
    symbol = input("Please enter the stock symbols of your choice. When done, type 'done': ")
    
    if float(len(symbol)) <= 5:
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
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
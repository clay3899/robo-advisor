
from dotenv import load_dotenv
import os
import json
import requests

from app.robo_advisor import compile_url, to_usd, get_response, parse_response, transform_parsed, write_to_csv


def test_to_usd():

    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_compile_url():

    # take a symbol and an API key. Input it into the URL

    symbol = "MSFT"
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", default ="OOPS")


    url = compile_url(symbol, api_key)
    assert url == f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

def test_get_response():
    
    # Checks to see if a success a website is reached through the URL

    symbol = "MSFT"
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", default ="OOPS")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    response = get_response(request_url)
    stringed_response = str(response)
    assert stringed_response == "<Response [200]>"

def test_parse_response():
    
    # tests for parsed results with the URL

    symbol = "MSFT"
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", default ="OOPS")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    
    response = get_response(request_url)

    parsed_response = parse_response(response)

    assert parsed_response == json.loads(response.text)

def test_transform_parsed():
    symbol = "MSFT"
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", default ="OOPS")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    
    response = get_response(request_url)

    parsed_response = parse_response(response)

    transform = transform_parsed(parsed_response)

    valid = ""

    if "close" in transform[0]:
        valid = "its transformed"


    assert valid == "its transformed"

def test_write_to_csv():


    symbol = "MSFT"
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", default ="OOPS")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    
    response = get_response(request_url)

    parsed_response = parse_response(response)

    transform = transform_parsed(parsed_response)

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "testing", f"{symbol}.csv")


    wow = write_to_csv(transform, csv_filepath)

    assert wow == True
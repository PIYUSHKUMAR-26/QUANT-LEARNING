# Mini Stock Screener (India) — Python + yfinance

A simple command-line stock screener that fetches key financial metrics for selected Indian stocks using pandas and yfinance, then filters them based on P/E ratio and Dividend Yield.

## Features
- Fetches: Company Name, Current Price, Trailing P/E Ratio, Dividend Yield
- Works with any NSE tickers (e.g., RELIANCE.NS, TCS.NS, INFY.NS)
- User inputs: maximum P/E ratio and minimum dividend yield
- Outputs a clean, readable table
- Handles missing data and fetch errors gracefully

## How It Works
1. A list of NSE stock tickers is defined inside the script.
2. Data is fetched using yfinance.Ticker().info.
3. The user enters filter values:
   - Max P/E ratio
   - Min dividend yield (decimal format, e.g., 0.02 = 2%)
4. The script filters the DataFrame and prints matching stocks.

## Project Structure
MINI STOCK SCREENER.py  
- get_stock_data(): fetches metrics for each ticker  
- main(): handles user input and filtering  
- __main__: runs the screener  

## Usage
Run the script:

python "MINI STOCK SCREENER.py"

Then enter values when prompted, for example:

Enter maximum P/E Ratio (e.g., 30.0): 25  
Enter minimum Dividend Yield (e.g., 0.01 for 1%): 0.02  

If matches exist, you’ll see output like:

--- SCREENING RESULTS ---  
Ticker   Company Name        Price   P/E Ratio   Dividend Yield  
TCS.NS   Tata Consultancy    3835.0  24.8        1.23%  

If no stocks match, the script tells you.

## Requirements
pip install pandas yfinance

## Default Tickers
RELIANCE.NS  
TCS.NS  
HDFCBANK.NS  
ICICIBANK.NS  
INFY.NS  
WIPRO.NS  
TITAN.NS  
BAJFINANCE.NS  

## Notes
- Dividend yield is expected as a decimal (e.g., 0.02 = 2%).  
- Yahoo Finance may return missing fields; these appear as N/A.  
- This is a beginner-friendly project focused on simplicity.

## License
Open source — free to use and modify.

import pandas as pd
import yfinance as yf

def get_stock_data(tickers):
    """
    Fetches key financial metrics for a list of stock tickers from yfinance.
    
    Args:
        tickers (list): A list of stock ticker symbols with the .NS suffix.
        
    Returns:
        pandas.DataFrame: A DataFrame with stock data.
    """
    stock_data = []
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            stock_data.append({
                'Ticker': ticker,
                'Company Name': info.get('longName', 'N/A'),
                'Price': info.get('currentPrice', 'N/A'),
                'P/E Ratio': info.get('trailingPE', 'N/A'),
                'Dividend Yield': info.get('dividendYield', 'N/A')
            })
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            
    return pd.DataFrame(stock_data)

def main():
    """Main function to run the stock screener."""
    
    TICKERS = [
        'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 
        'INFY.NS', 'WIPRO.NS', 'TITAN.NS', 'BAJFINANCE.NS'
    ]
    
    print("Welcome to your Mini Indian Stock Screener!")
    print("Fetching data from Yahoo Finance...")
    
    df = get_stock_data(TICKERS)
    
    if df.empty:
        print("Failed to fetch stock data. Please check your internet connection or the ticker list.")
        return
    
    print("\nData fetched successfully!")

    try:
        max_pe = float(input("Enter maximum P/E Ratio (e.g., 30.0): "))
        min_div_yield = float(input("Enter minimum Dividend Yield (e.g., 0.01 for 1%): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Filter the data based on your criteria, handling missing values
    results_df = df[
        (pd.to_numeric(df['P/E Ratio'], errors='coerce') <= max_pe) & 
        (pd.to_numeric(df['Dividend Yield'], errors='coerce') >= min_div_yield)
    ]

    print("\n--- SCREENING RESULTS ---")
    if not results_df.empty:
        # Format the output for better readability
        results_df['Dividend Yield'] = results_df['Dividend Yield'].apply(
            lambda x: f"{x:.2%}" if isinstance(x, (int, float)) else 'N/A'
        )
        print(results_df.to_string(index=False))
    else:
        print("No stocks matched your screening criteria.")
        
    print("-------------------------")

if __name__ == "__main__":
    main()
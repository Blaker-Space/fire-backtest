import json
from helpers.greetUser import greetUser
from helpers.fullBacktest import fullBacktest
from helpers.hypotheticalComparison import hypotheticalComparison

def main():
    greetUser()
    # Variables:
    mode = input("Select Mode - (1) Full Backtest, (2) Hypothetical Comparison: ")
    while(mode not in ['1', '2']):
        mode = input("Invalid input. Please select Mode - (1) Full Backtest, (2) Hypothetical Comparison: ")
    sp500Data = {} # S&P 500 yearly historical data including "year", "return_percent", and "dividend_percent"

    # Annual Return Percent was taken from MacroTrends: https://www.macrotrends.net/2526/sp-500-historical-annual-returns
    # Annual Dividend Yield was taken from Multpl: https://www.multpl.com/s-p-500-dividend-yield/table/by-year
    with open('data/sp-data.json', 'r') as f:
        sp500Data = json.load(f)
    
    if(mode == '1'):
        fullBacktest(sp500Data)
    elif(mode == '2'):
        hypotheticalComparison(sp500Data)
    else:
        print("Error: Invalid mode selected. Try running again and entering either '1' or '2'.")

if __name__ == "__main__":
    main()
import json

def main():
    data = {}
    average = 0.0
    # This data was taken from MacroTrends: 
    # https://www.macrotrends.net/2526/sp-500-historical-annual-returns
    with open('data/sp-data.json', 'r') as f:
        data = json.load(f)
    
    for data in data:
        average += data['return_percent']

    print(f"{average}")
    average /= len(data)
    print(f"Average S&P 500 return: {average:.2f}%")

if __name__ == "__main__":
    main()
import pandas as pd
def fullBacktest(sp500Data):
    print("Here is the full backtest results:")
    print("Legend:\nX-Axis: Starting FIRE Year\nY-Axis: Number of Years since starting FIRE Year\nData in Cells: Percentage difference between ABS FIRE and Traditional FIRE in relation to ABS FIRE")
    numYears = 1
    earliestYear = -1
    latestYear = -1
    
    for entry in sp500Data:
        year = entry['year']
        if earliestYear == -1 or year < earliestYear:
            earliestYear = year
        if latestYear == -1 or year > latestYear:
            latestYear = year

    numYears = latestYear - earliestYear + 1

    years = list(range(earliestYear, latestYear + 1))
    df = pd.DataFrame(columns=years, index=range(numYears))
    print(df)
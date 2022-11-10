import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,8))
    ax.scatter(df['Year'], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    x_pred = pd.Series([i for i in range(1880, 2051)])
    res = linregress(x=df['Year'], y=df["CSIRO Adjusted Sea Level"]) 
    ax.plot(x_pred, (res.intercept + res.slope*x_pred), color='r', linewidth=2)
    
    # Create second line of best fit
    x_2000 = df['Year'][df['Year']>=2000]
    y_2000 = df['CSIRO Adjusted Sea Level'][df['Year']>=2000]

    res_2000 = linregress(x = x_2000, y = y_2000)

    x_2000_pred = pd.Series([i for i in range(2000, 2051)])

    ax.plot(x_2000_pred, (res_2000.intercept + res_2000.slope*x_2000_pred), color='g', linewidth=2)
    

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
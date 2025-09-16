import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot(show_plot=False):
   
    
    # Clear any previous plots
    plt.clf()

    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot of historical data
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (all data)
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = list(range(df['Year'].min(), 2051))
    plt.plot(years_all, [(slope*x + intercept) for x in years_all], 'r', label='Fit: All data')

    # Second line of best fit (year >= 2000)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = list(range(2000, 2051))
    plt.plot(years_recent, [(slope2*x + intercept2) for x in years_recent], 'g', label='Fit: 2000 onwards')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')

    # Show plot only if requested
    if show_plot:
        plt.show()

    # Return axes object for testing
    return plt.gca()

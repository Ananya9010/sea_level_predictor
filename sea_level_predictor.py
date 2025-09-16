import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = list(range(df['Year'].min(), 2051))
    plt.plot(years, [(slope*x + intercept) for x in years], 'r')

    # Create second line of best fit (year >= 2000)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = list(range(2000, 2051))
    plt.plot(years_recent, [(slope2*x + intercept2) for x in years_recent], 'g')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

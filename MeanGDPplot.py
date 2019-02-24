#!/usr/bin/env python

"""
This is MeanGDPplot.py this script uses gapminder.txt to calculate and plot mean GDP
"""

# Import statements
import pandas as pd
import matplotlib.pyplot as plt
import pylab

def getContinent(continent, df):
    my_continent = df[df.continent == continent]
    return my_continent

def getMean(columnName, df):
    mean_data = df.iloc[:, columnName].mean()
    return mean_data

def plotBar(continentsList, meandataList, ylabel, title, figureName):
    # Set figure width to 10 and height to 8
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 10
    fig_size[1] = 8
    plt.rcParams["figure.figsize"] = fig_size

    # Plot the graph with Y axis label and Title
    plt.bar(continentsList, meandataList, align='center')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(figureName)

    # For personal visualization:
    plt.show()

#Write a function called getMeanPerContinent() that will take continent,
#column_name and df parameters and output the mean of a user-specified column
# for user-specified continent?

def getMeanPerContinent(continent, columnName, df):
    my_continent = df[df.continent == continent]
    mean_data = df.iloc[my_continent, columnName].mean()

    # Call plotBar function
    plotBar(continents, mean_gdp, "GDP per Capita", "Title", "plotBar.png")

    return mean_data


# read data into python
my_file = pd.read_csv("gapminder.txt", sep="\t")

# select information about Africa
#Africa = getContinent("Africa", my_file)
# calculate the mean
#Africa_Mean = Africa.iloc[:, 5].mean()
#Africa_Mean = getMean(5, Africa)

# Do the same for Europe
#Europe = getContinent("Europe", my_file)
#Europe_Mean = Europe.iloc[:, 5].mean()
#Europe_Mean = getMean(5, Europe)

# Create a List to store the values
#continents = ["Africa", "Europe"]
#mean_gdp = [Africa_Mean, Europe_Mean]

getMeanPerContinent()

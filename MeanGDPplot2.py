#!/usr/bin/env python
"""
This is MeanGdpPlot.py

This script uses gapminder.txt to calculate and plot mean
GDP per capita for African and European Countries.

"""

#Import statements
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import sys


def getContinent(continent, df):
    my_continent = df[df.continent == continent]
    return my_continent

def getMean(column_name, df):
    meandata = df.iloc[:,column_name].mean()
    return meandata

def plot_bar(continents_list, meandata_list, y_label, title, figure_name):
    # Set figure width to 10 and height to 8
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 10
    fig_size[1] = 8
    plt.rcParams["figure.figsize"] = fig_size

    #Plot the graph with Y axis label and Title
    plt.bar(continents_list,meandata_list,align='center')
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(figure_name)

    # For personal visualization:
    plt.show()


def getMeanPerContinent(continent, column_name, df):
    my_continent = getContinent(continent, df)
    meandata = getMean(column_name, my_continent)
    return meandata

file_name = sys.argv[1]

#read data into python
my_file = pd.read_csv(file_name, sep = "\t")

#select information about Africa
Africa_Mean = getMeanPerContinent('Africa', 5, my_file)

#Do the same for Europe
Europe_Mean = getMeanPerContinent('Europe', 5, my_file)

# Create a List to store the values
continents = ["Africa","Europe"]
mean_gdp = [Africa_Mean, Europe_Mean]

plot_bar(continents, mean_gdp, 'gdp per capita', 'this is the title', 'meangdp.png')
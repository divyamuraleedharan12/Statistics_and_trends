# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 20:18:17 2023

@author: divya
"""

import pandas as pd
import matplotlib.pyplot as plt


def read_data(filename):
    """
    The below function reads data and returns pandas dataframe object.
    """
    # Reads data from csv file
    dataframe = pd.read_csv(filename, skiprows=4)
    # Returns the dataframe
    return dataframe


def filter_data(dataframe, column, value, countries, years):
    """
    The below function is used to filter data and returns a dataframe and 
    transpose of the dataframe.
    """
    # Groups data with column value
    filtered_data = dataframe.groupby(column, group_keys=True)
    # Retrives the data
    filtered_data = filtered_data.get_group(value)
    # Resets the index
    filtered_data = filtered_data.reset_index()
    # Sets Country Name as the new index of the filtered_data
    filtered_data.set_index('Country Name', inplace=True)
    # filter the data from dataframe
    filtered_data = filtered_data.loc[:, years]
    filtered_data = filtered_data.loc[countries, :]
    # Drops the NAN values from dataframe
    filtered_data = filtered_data.dropna(axis=1)
    # Resets the index
    filtered_data = filtered_data.reset_index()
    # Transposing the index of the dataframe
    transposed_data = filtered_data.set_index('Country Name')
    transposed_data = transposed_data.transpose()
    # Returns normal dataframe and transposed dataframe
    return filtered_data, transposed_data


def bar_plot(dataset, title, xlabel, ylabel):
    """ 
    The function below is used to generate a bar plot.
    """
    # Creates a bar plot from the dataset DataFrame
    dataset.plot.bar(x='Country Name', rot=0, figsize=(50, 25), fontsize=50)
    # Sets the location of the y-axis ticks
    plt.yticks([0, 20, 40, 60, 80, 100])
    plt.legend(fontsize=50)
    # Sets title and font size for plot
    plt.title(title.upper(), fontsize=60, fontweight='bold')
    # Sets x-label and font size for plot axes
    plt.xlabel(xlabel, fontsize=60)
    # Sets y-label and font size for plot axes
    plt.ylabel(ylabel, fontsize=60)
    # Saves bar plot figure as png
    plt.savefig(title + '.png')
    # Function to show the plot
    plt.show()
    return


# Creating list of countries and years for plotting bar plot
country1 = ['Ethiopia', 'Peru', 'India', 'Nigeria']
year1 = ['2000', '2005', '2010', '2015', '2020']
# Reads data from csv file
world_data = read_data("climate_change.csv")
world_data1, transdata1 = filter_data(
    world_data, 'Indicator Name', 'Urban population (% of total population)', country1, year1)
# Prints filtered data and transposed data
print(world_data1)
print(transdata1)
# Calling bar plot function with indicator as Urban Population
bar_plot(world_data1, 'Urban population (% of total population)',
         'Countries', 'Percentage of Urban Population')

world_data2, transdata2 = filter_data(
    world_data, 'Indicator Name', 'Access to electricity (% of population)', country1, year1)

print(world_data2)
print(transdata2)
# Calling another bar plot function with indicator as Access to electricity
bar_plot(world_data2, 'Access to Electricity (% of population)',
         'Countries', 'Percentage of Electricity access')

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 20:18:17 2023

@author: divya
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def read_data(filename):
    """
    The below function reads data and returns pandas dataframe object.
    """
    # Reads data from csv file
    dataframe = pd.read_csv(filename, skiprows = 4)
    # Returns the dataframe
    return dataframe


def filter_data(dataframe, column, value, countries, years):
    """
    The below function is used to filter data and returns a dataframe and 
    transpose of the dataframe.
    """
    # Groups data with column value
    filtered_data = dataframe.groupby(column, group_keys = True)
    # Retrives the data
    filtered_data = filtered_data.get_group(value)
    # Resets the index
    filtered_data = filtered_data.reset_index()
    # Sets Country Name as the new index of the filtered_data
    filtered_data.set_index('Country Name', inplace = True)
    # filter the data from dataframe
    filtered_data = filtered_data.loc[:, years]
    filtered_data = filtered_data.loc[countries, :]
    # Drops the NAN values from dataframe
    filtered_data = filtered_data.dropna(axis = 1)
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
    dataset.plot.bar(x = 'Country Name', rot = 0, figsize = (50, 25), fontsize = 50)
    # Sets the location of the y-axis ticks
    plt.yticks([0, 20, 40, 60, 80, 100])
    plt.legend(fontsize = 50)
    # Sets title and font size for plot
    plt.title(title.upper(), fontsize = 60, fontweight = 'bold')
    # Sets x-label and font size for plot axes 
    plt.xlabel(xlabel, fontsize = 60)
    # Sets y-label and font size for plot axes
    plt.ylabel(ylabel, fontsize = 60)
    # Saves bar plot figure as png
    plt.savefig(title + '.png')
    # Function to show the plot
    plt.show()
    return

def line_plot(dataset, title, xlabel, ylabel):
    """ 
    The function below is used to generate a line plot.
    """
    # Creates a line plot from the dataset DataFrame
    dataset.plot.line(figsize = (50, 30), fontsize = 60, linewidth = 6.0)
    # Sets the location of the y-axis ticks
    plt.yticks([0,10,20,30,40,50,60,70,80])
    # Sets title and font size for plot
    plt.title(title.upper(), fontsize = 70, fontweight = 'bold')
    # Sets x-label and font size for plot axes
    plt.xlabel(xlabel, fontsize = 70)
    # Sets y-label and font size for plot axes
    plt.ylabel(ylabel, fontsize = 70)
    plt.legend(fontsize = 60)
    # Saves line plot figure as png
    plt.savefig(title + '.png')
    # Function to show the plot
    plt.show()
    return

def stat_data(dataframe, col, value, yr, a):
    """
    Reading a dataframe with multiple indicators and returns a dataframe
    where dataframe will be used for the Heat Map
    """
    # Groups the rows of dataframe by the values of the col column
    df3 = dataframe.groupby(col, group_keys=True)
    # Retrieves the data with group_by element
    df3 = df3.get_group(value)
    # Resets the index of the dataframe
    df3 = df3.reset_index()
    df3.set_index('Indicator Name', inplace=True)
    df3 = df3.loc[:, yr]
    #transposing the index of the dataframe
    df3 = df3.transpose()
    df3 = df3.loc[:, a]
    return df3  # returns dataframe required for Heatmap


def heat_map(data):
    """
    The below function visualizes correlation between different indicators.
    """
    plt.figure(figsize = (60, 40))
    sns.heatmap(data.corr(), annot = True, annot_kws = {"size":32})
    # Sets title for plot
    plt.title("Brazil's Heatmap".upper(), size = 40, fontweight = 'bold')
    plt.xticks(rotation = 90, horizontalalignment = "center", fontsize = 40)
    plt.yticks(rotation = 0, fontsize = 40)
    #saving Heatmap image as png
    plt.savefig('Heatmap.png', dpi = 300, bbox_inches = 'tight')
    plt.show()
    return data

# Creating list of countries and years for plotting bar plot
country1 = ['Ethiopia', 'Peru', 'India', 'Nigeria','Angola']
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
# Prints filtered data and transposed data
print(world_data2)
print(transdata2)

# Calling another bar plot function with indicator as Access to electricity
bar_plot(world_data2, 'Access to Electricity (% of population)',
         'Countries', 'Percentage of Electricity access')
# Creating list of countries and years for plotting line plot
country2 = ['Vietnam', 'Sri Lanka', 'Pakistan', 'Bulgaria', 'Cuba']
year2 = ['1990', '1995', '2000', '2005', '2010']
world_data3, transdata3 = filter_data(
    world_data, 'Indicator Name', 'Agricultural land (% of land area)', country2, year2)
# Prints filtered data and transposed data
print(world_data3)
print(transdata3)

# Calling line plot function with indicator as Agricultural land
line_plot(transdata3, 'Agricultural land (% of land area)',
          'Year', 'Agricultural land (% of land area)')

world_data4, transdata4 = filter_data(
    world_data, 'Indicator Name', 'Arable land (% of land area)', country2, year2)
# Prints filtered data and transposed data
print(world_data4)
print(transdata4)

# Calling another line plot function with indicator as Forest land
line_plot(transdata4, 'Arable land (% of land area)',
          'Year', 'Arable land (% of land area)')

# Creating a variable with years
year_heat = ['2000', '2004', '2008', '2012', '2016']
#creating a variable indicators for HeatMap
indicators = ['Arable land (% of land area)', 'Agricultural land (% of land area)', 
              'Urban population (% of total population)','Access to electricity (% of population)', 'Cereal yield (kg per hectare)', 'Annual freshwater withdrawals, total (% of internal resources)']
dataheat = stat_data(world_data, 'Country Name',
                     'Brazil', year_heat, indicators)
print(dataheat.head())
#Calling a function to create heatmap
heat_map(dataheat)

start = 2000
end = 2020
yeardes = [str(i) for i in range(start, end+1)]
indicator2 = ['Population growth (annual %)', 'Electricity production from oil sources (% of total)',
              'CO2 emissions from solid fuel consumption (% of total)', 'Electricity production from natural gas sources (% of total)']
descr = stat_data(world_data, 'Country Name',
                'United Arab Emirates', yeardes, indicator2)
# returns a summary of descriptive statistics for a dataset
stats_summary = descr.describe()
print(stats_summary)
skewness = stats.skew(descr['Population growth (annual %)'])
kurtosis = descr['Electricity production from oil sources (% of total)'].kurtosis()
print('Skewness of Population growth in United Arab Emirates : ', skewness)
print('Kurtosis of Electricity production from natural gas in United Arab Emirates : ', kurtosis)
# saves result to a csv file
stats_summary.to_csv('statistics_report.csv')
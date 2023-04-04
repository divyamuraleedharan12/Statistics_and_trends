# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 20:18:17 2023

@author: divya
"""

import pandas as pd


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

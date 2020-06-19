'''
This module provides a function which plots a map using data from a pandas DataFrame
'''

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas

def display_tallinn_map(merged_data_frame: pandas.DataFrame):
    '''
    This function renders a map of europe and plots
    a direct flightpath from Source (Tallinn) to destination
    @Param merged_data_frame -- a pandas dataframe containing coordinates
                        and IATA code of destinations
    @return None
    '''
    data_frame = merged_data_frame
    # get one row containing information about TLL airport
    tallinn = data_frame.loc[data_frame['IATA'] == "TLL"]
    tl_lat = tallinn['Latitude'][0]
    tl_lon = tallinn['Longitude'][0]

    # longitude range: -20E (20W) to 60E, latitude range: 30N to 60N
    extent = [-20, 60, 30, 60]  # extent contains the longitude and latitude

    # plt the map
    axes = plt.axes(projection=ccrs.PlateCarree())
    axes.set_extent(extent)
    axes.stock_img()
    axes.coastlines()

    # plot destination with lines
    for index, row in data_frame.iterrows():
        plt.plot(
            [tl_lon, row['Longitude']], [tl_lat, row['Latitude']],
            color='blue',
            linewidth=1,
            marker='1',
            transform=ccrs.Geodetic())

        plt.text(
            row['Longitude'], row['Latitude'] + 0.4, row['City_x'],
            horizontalalignment='right',
            transform=ccrs.Geodetic(),
            color="black")

    plt.title("List of cities with direct flight to tallinn")
    plt.savefig('./pics/map.png')

    plt.show()

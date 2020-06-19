#!/usr/bin/env python

'''
Main module to plot direct flight path froms tallinn
'''

from flightpath.tallinn import display_tallinn_map
import pandas


def read_data() -> pandas.DataFrame:
    '''
    This functions reads 2 CSV files of airports and coordiates
    @returns pandas.DataFrame, merged dataframe of direct airports
             and their coordinates
    '''
    # import airport corrdinates
    airport_coords = pandas.read_csv("./data/airports.csv")
    # import list of airports with direct flight to Tallinn
    direct_flights = pandas.read_csv("./data/otselennud.csv", delimiter=";")
    # merge the two one the basis of IATA code
    direct_flight_coords = direct_flights.merge(airport_coords, on="IATA")
    # optional, save merged data to a serperate CSV file (for debugging purposes)
    # direct_flight_coords.to_csv("./data/mergedData.csv")

    return direct_flight_coords


if __name__ == '__main__':
    DF = read_data()
    display_tallinn_map(DF)

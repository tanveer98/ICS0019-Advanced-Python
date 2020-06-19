# Homework 3 
## Objctive of this homework is to display cities that have a direct flight to tallinn

To run the program, use main.py.

The main function reads the CSV files, merges them to create a 'joined' DataFrame.

That DataFrame is sent to the display_tallinn_map function, which gets the latitude and longitudes of the cites and displays with using cartopy and matplotlib. The display_tallinn_map function resides under the flightpath packges tallinn module.

The pictures can be found on the ./pics directory

The csv files can be found on the ./data directory
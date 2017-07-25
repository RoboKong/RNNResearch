# Script to read a standard csv file
import csv
# Opens Test.csv to be read with 'r'
with open('test.csv', 'r') as csvfile:
    # The default delimiter is a comma
    creader = csv.reader(csvfile, delimiter=',')
    for row in creader:
        # Takes and prints each row to console adding a
        # comma where the delimiter (comma in this case) was.
        print ','.join(row)

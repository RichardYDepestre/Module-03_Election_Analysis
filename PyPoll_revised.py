# the data that we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import time
import os
from clear_screen import screen_clear
# import the datetime class from the datetime module.
import datetime as dt
import random
import csv

screen_clear()
#   use the now() attribute on the datetime class ato get the present time
present_time = dt.datetime.now()
print(f'the time right now is -> {present_time}\n')
# print(dir(csv))

election_counties = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
# print(dir(election_counties))
# print(f'\n{dir(random)}')

#   assign a variable for the file to load and the path.
file_to_load = os.path.join("~Resources", "election_results.csv")
# open file
election_data = open(file_to_load, 'r')

# close file
if not(election_data.closed):
    election_data.close()
print(election_data.closed)

#   Python has a way to read and write to a file without needing to use the open() and
#   close() functions every time.
#   We simply replace the open() function with the 'with' statement.
#   The with statement opens the file and ensures proper acquisition or release of any data
#   without having to close the file, to ensure that the data isn't lost or corrupted.
with open(file_to_load) as election_data:
    line = election_data.readlines()
print(election_data)
print(election_data.closed)

#   indirect file path
#   To access and open a file for which the direct path is unknown, we use the os module.
dir(os.path)
dir(os.curdir)
#   To declare a variable for the file to load, connect the os.path submodule with the join()
#   function, like this: os.path.join().
#   This is called chaining.
#   Chaining is a programmatic style that is used for making multiple method calls on the
#   same object. This is a common practice that makes code look clean and concise.
#   Inside the parentheses of the join() function, we will add the folder and file to join
#   together. In this case, we'll add the Resources folder and election_results.csv separated
#   by a comma, like this:
#   os.path.join("Resources", "election_results.csv")
file_to_load = os.path.join('~resources', 'election_results.csv')
print(f'file to load -> {file_to_load}')
#   version 1
start_time = time.time()
with open(file_to_load) as election_data:
    headers = next(election_data)
    print(f'\nheader -> {headers}')
    # dir(file_to_load)
    #   to read and analyze the data here
    # lines = election_data.readlines()
    # print(lines)
    file_reader = csv.reader(election_data)
    #   now print each row of the file reader object
    for line in file_reader:
        print(line)
print("--- %s seconds ---" % (time.time() - start_time))
#   version 2
# with open(file_to_load) as election_data:
#     #   to read and analyze the data here
#     lines = election_data.read().splitlines()
#     election_data.close()
#     #   file_reader = csv.reader(election_data)
#     #   now print each row of the file reader object
#     for line in lines:
#         print(line[0])  # print(election_data)

# ##  Writing to a file!  ##
# #   create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join('~analysis', 'election_analysis.txt')
# print(f'file to save -> {file_to_save}')
# #   using the with statement open thefile as a text file.
# file_handle = open(file_to_save, 'w')
# #   write some data to the file

# file_handle.write(
#     f'{"Counties in the Election"}\n{"-"*len("Counties in the Election")}\n')
# for county in election_counties:
#     # print(county)
#     # print(election_counties[county])
#     if county != 'Jefferson':
#         text = county + ', '
#         file_handle.write(text)
#     else:
#         file_handle.write(county)
# #   close the file
# file_handle.close()
# #   is the file closed?
# if file_handle.closed:
#     print(f'file "{file_to_save}" has been closed.')  # file_handle.closed)
# # with open(file_to_save) as election_analysis:
# # lines = election_analysis.write().splitlines()
# # print(lines)
# # print(election_analysis)

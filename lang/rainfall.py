# import data into a numpy array

import numpy as np

data_array = np.genfromtxt("python_language_1_data.csv", delimiter=",", names=True,
                            dtype=[int, int, float])

rainfall = "rainfall_mmday"

# store end years
first_year = data_array[0][0]
last_year = data_array[-1][0]

# create a year key for dictionary
year_tuple = tuple(range(first_year, last_year + 1))

# create dictionary, with year keys and empty list values
data_dic = {}

for year in year_tuple:
    data_dic[year] = []    

# iterate through rows, adding rainfall data to appropriate year list of dictionary
'''
# alternative version
for day in range(data_array.size):
    data_dic[data_array[day][0]].append(data_array[day][2])
'''
for day in data_array:
    data_dic[day[0]].append(day[2])


#export dictionary to json

import json

with open('python_language_1_data.json', 'w') as json_file:
    json.dump(data_dic, json_file, indent=4)

# function to create a plot in png format of rainfall across a year,
# takes a json file, year, and optional colour
    
from matplotlib import pyplot as plt

def plot_from_json(filename, year, colour='green'):
    
    with open(filename, 'r') as f:
        temp_string = f.read()
        
    plot_data_dic = json.loads(temp_string)
    plot_data = plot_data_dic[year]
    
    year_graph, year_graph_axes = plt.subplots()
    
    # attempt to plot graph, raise error if colour input is invalid
    try:
        year_graph_axes.plot(plot_data, color = colour)
    except ValueError:
        pass
    
    year_graph_axes.set_title("Average daily rainfall for 1988")
    year_graph_axes.set_ylabel("rainfall / mmday")
    year_graph_axes.set_xlabel("day")
    
    # save as .png
    year_graph.savefig('year_rainfall_graph.png')

#plot a chart for 1998, and export plot as png file, with magenta line    
plot_from_json('python_language_1_data.json', '1998', 'magenta')


#write a function to plot a graph of yearly mean rainfall for a custom period
def mean_from_list(num_list):
    return (sum(num_list) / len(num_list))

def yearly_mean_plot(filename, start_year, end_year):
    
    with open(filename, 'r') as f:
        temp_string = f.read()

    plot_data_dic = json.loads(temp_string)
    
    cust_year_list = list(range(int(start_year), int(end_year) + 1))    
    year_mean_list = []
    for year in cust_year_list:
        year_mean = mean_from_list(plot_data_dic[str(year)])
        year_mean_list.append(year_mean)
    
    custom_graph, custom_graph_axes = plt.subplots()
    
    custom_graph_axes.plot(cust_year_list, year_mean_list)
    
    custom_graph_axes.set_title("Yearly rainfall averages from {} to {}".format(start_year, end_year))
    custom_graph_axes.set_ylabel("average rainfall / mm per day")
    custom_graph_axes.set_xlabel("year")
    
    # save as .png   custom_graph.savefig('custom_rainfall_graph.png')
    custom_graph.savefig('mean_rainfall_graph.png')

#prod a plot 1988-2000 inclusive
yearly_mean_plot('python_language_1_data.json', '1988', '2000')



# function to apply correction code: (rainfall_value * 1.2 ^ root(2))
def rain_corrector(rain_value):
    root_two = 2**(1/2)
    correct_rain_value = rain_value * (1.2 ** root_two) 
    return correct_rain_value

# function to correct all of the data for a given year (v1 - using a for loop)
def year_corrector_loop(filename, year):
    # import dictionary
    with open(filename, 'r') as f:
        temp_string = f.read()
    bad_data_dic = json.loads(temp_string)
    
    for v_index in range(len(bad_data_dic[year])):
        bad_entry = bad_data_dic[year][v_index]
        fixed_entry = rain_corrector(bad_entry)
        bad_data_dic[year][v_index] = fixed_entry
        
#    for rain_value in bad_data_dic[str(year)]:
#        bad_data_dic[str(year)][v_index] = rain_corrector(day)
        
        
    with open('fixed_rain_data_loop.json', 'w') as fixed_json_file:
        json.dump(bad_data_dic, fixed_json_file, indent=4)
        
# test corrector loop version
year_corrector_loop('python_language_1_data.json', '2000')

# function to correct all of the data for a given year (v2 - using a list comp)
def year_corrector_comp(filename, year):
    # import dictionary
    with open(filename, 'r') as f:
        temp_string = f.read()
    bad_data_dic = json.loads(temp_string)
    
    fixed_year = [rain_corrector(entry) for entry in bad_data_dic[year]]
    
    bad_data_dic[year] = fixed_year
    
    with open('fixed_rain_data_comp.json', 'w') as fixed_json_file:
        json.dump(bad_data_dic, fixed_json_file, indent=4)

# test corrector comp version
year_corrector_comp('python_language_1_data.json', '1942')
'''
The loop version benefits from spreading out the operations,
which can make them easier to follow.

The list comprehension version benefits from conciseness,
and general readibility
'''


'''
spare code:
    #clear figure
    year_graph.clf()

'''
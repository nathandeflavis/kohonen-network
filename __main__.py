"""
A module that is the entry point into the program,
responsible for getting user input
and passing data points to the 'kohonen' module.
"""
from kohonen import *
from vector import *
from csv import *
from copy import *

"""
A function that is the entry point into the program.
"""
def main():
    training_set = "Training"
    test_set = "Test"
    prompt = "Use <" + training_set + "> set or <" + test_set + "> set? "
    set_to_use = input(prompt)    
    set_file_path = get_set_file_path(set_to_use)
    
    data_points_to_normalise = get_data_points(set_file_path)
    data_points_not_to_normalise = deepcopy(data_points_to_normalise)

    first_data_point_to_normalise_index = 0
    first_data_point_to_normalise = data_points_to_normalise[
        first_data_point_to_normalise_index]
    units = get_units(first_data_point_to_normalise)
    use_training_set = set_to_use == training_set

    if use_training_set:
        train(data_points_to_normalise, units)
    
    cluster(data_points_not_to_normalise, units)

"""
A function to get a training/test set file's path for a set's given name.
"""
def get_set_file_path(set_to_use):
    directory = "Sets"
    file_extension = "csv"
    set_file_path = directory + "/" + set_to_use + "." + file_extension
    return set_file_path

def test_get_set_file_path():
    set_to_use = "Training"
    set_file_path = get_set_file_path(set_to_use)
    directory = "Sets"
    file_extension = "csv"
    assert set_file_path == directory + "/" + set_to_use + "." + file_extension

"""
A function to extract data points from a training/test set file
with a given path.
"""
def get_data_points(set_file_path):
    data_points = []
    
    with open(set_file_path) as file:
        reader = DictReader(file)
        
        for line in reader:
            data_point = get_data_point(line)
            data_points.append(data_point)
                
    file.close()
    return data_points

"""
A function to extract a data point
from a given line of a training/test set file.
"""
def get_data_point(set_file_line):
    coordinates = []
    values = set_file_line.values()
    
    for value in values:
        coordinate = float(value)
        coordinates.append(coordinate)

    data_point = Vector(coordinates)
    return data_point

"""
A function to generate Kohonen units
with the dimensionality of a given data point.
"""
def get_units(data_point):
    units = []
    prompt = "How many units? "
    start = 0
    unit_count = int(input(prompt))

    for i in range(start, unit_count):
        unit_number = i + 1
        output = "Unit " + str(unit_number) + ":"
        print(output)
        
        unit = get_unit(data_point)
        units.append(unit)

    return units

"""
A function to generate a Kohonen unit
with the dimensionality of a given data point. 
"""
def get_unit(data_point):
    start = 0
    data_point_coordinates = data_point._coordinates
    data_point_dimensionality = len(data_point_coordinates)
    unit_coordinates = []

    for j in range(start, data_point_dimensionality):
        unit_coordinate_number = j + 1
        prompt = "Coordinate " + str(unit_coordinate_number) + ": "
        unit_coordinate = float(input(prompt))
        unit_coordinates.append(unit_coordinate)

    unit = Vector(unit_coordinates)
    return unit

main()

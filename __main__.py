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
    trainingSet = "Training"
    testSet = "Test"
    prompt = "Use <" + trainingSet + "> set or <" + testSet + "> set? "
    setToUse = input(prompt)    
    setFilePath = get_set_file_path(setToUse)
    
    dataPointsToNormalise = get_data_points(setFilePath)
    dataPointsNotToNormalise = deepcopy(dataPointsToNormalise)

    firstDataPointToNormaliseIndex = 0
    firstDataPointToNormalise = dataPointsToNormalise[
        firstDataPointToNormaliseIndex]
    units = get_units(firstDataPointToNormalise)
    useTrainingSet = setToUse == trainingSet

    if useTrainingSet:
        train(dataPointsToNormalise, units)
    
    cluster(dataPointsNotToNormalise, units)

"""
A function to get a training/test set file's path given the set's name.
"""
def get_set_file_path(setToUse):
    directory = "Sets"
    fileExtension = "csv"
    setFilePath = directory + "/" + setToUse + "." + fileExtension
    return setFilePath

"""
A function to extract data points from a training/test set file
with a given path.
"""
def get_data_points(setFilePath):
    dataPoints = []
    
    with open(setFilePath) as file:
        reader = DictReader(file)
        
        for line in reader:
            dataPoint = get_data_point(line)
            dataPoints.append(dataPoint)
                
    file.close()
    return dataPoints

"""
A function to extract a data point
from a given line of a training/test set file.
"""
def get_data_point(setFileLine):
    coordinates = []
    values = setFileLine.values()
    
    for value in values:
        coordinate = float(value)
        coordinates.append(coordinate)

    dataPoint = Vector(coordinates)
    return dataPoint

"""
A function to generate Kohonen units
with the dimensionality of a given data point.
"""
def get_units(dataPoint):
    units = []
    prompt = "How many units? "
    start = 0
    unitCount = int(input(prompt))

    for i in range(start, unitCount):
        unitNumber = i + 1
        output = "Unit " + str(unitNumber) + ":"
        print(output)
        
        unit = get_unit(dataPoint)
        units.append(unit)

    return units

"""
A function to generate a Kohonen unit
with dimensionality of a given data point. 
"""
def get_unit(dataPoint):
    start = 0
    dataPointCoordinates = dataPoint._coordinates
    dataPointDimensionality = len(dataPointCoordinates)
    unitCoordinates = []

    for j in range(start, dataPointDimensionality):
        unitCoordinateNumber = j + 1
        prompt = "Coordinate " + str(unitCoordinateNumber) + ": "
        unitCoordinate = float(input(prompt))
        unitCoordinates.append(unitCoordinate)

    unit = Vector(unitCoordinates)
    return unit

main()

"""
A module that is the entry point into the program,
responsible for getting user input
and passing data points to the 'kohonen' module.
"""
from kohonen import *
from vector import *
from csv import *

"""
A function that is the entry point into the program.
"""
def main():
    prompt = "Use <Training> or <Test> set? "
    setToUse = input(prompt)
    directory = "Sets"
    fileExtension = "csv"
    dataFilePath = directory + "/" + setToUse + "." + fileExtension
    dataPointsToNormalise = get_data_points(dataFilePath)
    
    #deep copy
    dataPointsNotToNormalise = []

    for dataPoint in dataPointsToNormalise:
        coordinates = []

        for coordinate in dataPoint.get_coordinates():
            coordinates.append(coordinate)

        dataPointsNotToNormalise.append(Vector(coordinates))

    firstDataPointToNormaliseIndex = 0
    firstDataPointToNormalise = dataPointsToNormalise[
        firstDataPointToNormaliseIndex]
    units = get_units(firstDataPointToNormalise)
    useTrainingSet = setToUse == "Training"

    if useTrainingSet:
        train(dataPointsToNormalise, units)
    
    cluster(dataPointsNotToNormalise, units)

"""
A function to extract data points from a data file with a given path.
"""
def get_data_points(dataFilePath):
    dataPoints = []
    
    with open(dataFilePath) as file:
        for line in DictReader(file):
            coordinates = []
            values = line.values()
            
            for value in values:
                coordinates.append(float(value))

            dataPoint = Vector(coordinates)
            dataPoints.append(dataPoint)
                
    file.close()
    return dataPoints

"""
A function to generate Kohonen units
with the dimensionality of a given data point.
"""
def get_units(dataPoint):
    units = []
    prompt = "How many units? "
    start = 0

    for i in range(start, int(input(prompt))):
        unitNumber = i + 1
        output = "Unit " + str(unitNumber) + ":"
        print(output)
        
        coordinates = []
        dataPointDimensionality = len(dataPoint._coordinates)

        for j in range(start, dataPointDimensionality):
            coordinateNumber = j + 1
            prompt = "Coordinate " + str(coordinateNumber) + ": "
            coordinate = float(input(prompt))
            coordinates.append(coordinate)

        unit = Vector(coordinates)
        units.append(unit)

    return units

main()

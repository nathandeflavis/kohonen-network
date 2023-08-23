from kohonen import *
from vector import *
from csv import *

def main():
    setToUse = input("Use <Training> or <Test> set? ")
    dataPointsToNormalise = get_data_points("Sets/" + setToUse + ".csv")
    #deep copy
    dataPointsNotToNormalise = []

    for dataPoint in dataPointsToNormalise:
        coordinates = []

        for coordinate in dataPoint.get_coordinates():
            coordinates.append(coordinate)
        
        dataPointsNotToNormalise.append(Vector(coordinates))

    units = get_units(dataPointsToNormalise[0])

    if setToUse == "Training":
        train(dataPointsToNormalise, units)
    
    cluster(dataPointsNotToNormalise, units)

def get_data_points(dataFilePath):
    dataPoints = []
    
    with open(dataFilePath) as file:
        for line in DictReader(file):
            coordinates = []
            
            for value in line.values():
                coordinates.append(float(value))

            dataPoints.append(Vector(coordinates))
                
    file.close()
    return dataPoints

#sample data point
def get_units(dataPoint):
    units = []

    for i in range(0, int(input("How many units? "))):
        print("Unit " + str(i + 1) + ":")
        coordinates = []

        for j in range(0, len(dataPoint._coordinates)):
            coordinates.append(float(input("Coordinate " + str(j + 1) + ": ")))

        units.append(Vector(coordinates))

    return units

main()

"""
A module that is an implementation of the Kohonen layer
of a Kohonen-Grossberg counter-propagation network,
responsible for training it
and clustering the data points received from the main module.
"""
from vector import *

"""
A function to train a Kohonen network with given Kohonen units
by inputting given data points into the network.
"""
def train(dataPoints, units):
    for dataPoint in dataPoints:
        dataPoint.normalise()

    for unit in units:
        unit.normalise()

    done = False
    epoch = 1
    sigmasEpoch = []

    while not done:
        output = "Epoch " + str(epoch)
        print(output)
        
        output = "Iteration weight changes:"
        print(output)
        
        sigmaEpoch = 0
        start = 0
        dataPointCount = len(dataPoints)
        
        #choose training example (sequentially)
        for i in range(start, dataPointCount):
            dataPoint = dataPoints[i]
            unit = get_nearest_unit(dataPoint, units)
            
            #deep copy
            unitCoordinates = unit.get_coordinates()[:]
            
            delta = Vector(unitCoordinates)
            multiplier = -1
            delta.multiply_by(multiplier)
            delta.add(dataPoint)
            
            learningRate = 0.1
            delta.multiply_by(learningRate)
            
            sigmaIteration = 0
            deltaCoordinates = delta.get_coordinates()

            for coordinate in deltaCoordinates:
                sigmaIteration += abs(coordinate)

            output = str(sigmaIteration)
            print(output)
            
            sigmaEpoch += sigmaIteration
            unit.add(delta)
            unit.normalise()
            
            minWeightChange = .01
            sigmaIterationIsTooSmall = sigmaIteration < minWeightChange

            if sigmaIterationIsTooSmall:
                done = True
                break

        sigmasEpoch.append(sigmaEpoch)
        epoch += 1

    output = "Epoch weight changes:"
    print(output)

    for sigmaEpoch in sigmasEpoch:
        output = str(sigmaEpoch)
        print(output)

"""
A function to get the nearest of given Kohonen units
to a given data point.
"""
def get_nearest_unit(dataPoint, units):
    nets = []

    for unit in units:
        net = 0
        start = 0
        unitDimensionality = len(unit.get_coordinates())
        
        for i in range(start, unitDimensionality):
            dataPointCoordinates = dataPoint.get_coordinates()
            dataPointCoordinate = dataPointCoordinates[i]

            unitCoordinates = unit.get_coordinates()
            unitCoordinate = unitCoordinates[i]
            
            product = dataPointCoordinate * unitCoordinate
            net += product

        nets.append(net)
        
    maxNet = max(nets)
    start = 0
    unitCount = len(units)

    for i in range(start, unitCount):
        net = nets[i]
        netIsMaxNet = net == maxNet
        
        if netIsMaxNet:
            unit = units[i]
            return unit

    return None

"""
A function to cluster given data points using given Kohonen units.
"""
def cluster(dataPoints, units):
    print("Data point clusters:")
    dataPointClusters = {}

    for dataPoint in dataPoints:
        unit = get_nearest_unit(dataPoint, units)
        unitIsInDataPointClusters = unit in dataPointClusters

        if unitIsInDataPointClusters:
            dataPointClusters[unit].append(str(dataPoint))
        else:
            dataPointClusters[unit] = [str(dataPoint)]

    keys = dataPointClusters.keys()

    for key in keys:
        output = "Cluster " + str(key) + ":"
        print(output)

        output = "Data points:"
        print(output)
        dataPointCluster = dataPointClusters[key]

        for dataPoint in dataPointCluster:
            output = str(dataPoint)
            print(output)

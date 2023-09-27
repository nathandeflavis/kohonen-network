"""
A module that is an implementation of the Kohonen layer
of a Kohonen-Grossberg counter-propagation network,
responsible for training it
and clustering the data points received from the main module.
"""
from vector import *
from copy import *

"""
A function to train a Kohonen network with given Kohonen units
by inputting given data points into the network.
"""
def train(dataPoints, units):
    normalise_vectors(dataPoints)
    normalise_vectors(units)
    epochWeightChangeSums = get_epoch_weight_change_sums(dataPoints, units);

    output = "Epoch weight changes:"
    print(output)
    print_epoch_weight_change_sums(epochWeightChangeSums)

"""
A function to normalise given vectors.
"""
def normalise_vectors(vectors):
    for vector in vectors:
        vector.normalise()

"""
A function to compute weight change sums in epochs
for given data points and Kohonen units.
"""
def get_epoch_weight_change_sums(dataPoints, units):
    globals()['networkIsTrained'] = False
    epoch = 1
    epochWeightChangeSums = []

    while not globals()['networkIsTrained']:
        output = "Epoch " + str(epoch)
        print(output)
        
        output = "Iteration weight changes:"
        print(output)
        
        epochWeightChangeSum = get_epoch_weight_change_sum(dataPoints, units)
        epochWeightChangeSums.append(epochWeightChangeSum)
        epoch += 1

    return epochWeightChangeSums

"""
A function to compute a weight change sum in an epoch
for given data points and Kohonen units.
"""
def get_epoch_weight_change_sum(dataPoints, units):
    epochWeightChangeSum = 0
    start = 0
    dataPointCount = len(dataPoints)
    
    #choose training example (sequentially)
    for i in range(start, dataPointCount):
        dataPoint = dataPoints[i]
        unit = get_nearest_unit(dataPoint, units)
        weightChange = get_weight_change(unit, dataPoint)            
        iterationWeightChangeSum = get_weight_change_sum(weightChange)
        #output = str(iterationWeightChangeSum)
        #print(output)

        epochWeightChangeSum += iterationWeightChangeSum
        unit.add(weightChange)
        unit.normalise()
        
        minWeightChange = .01
        iterationWeightChangeSumIsNegligible = iterationWeightChangeSum < minWeightChange

        if iterationWeightChangeSumIsNegligible:
            globals()['networkIsTrained'] = True
            break

    return epochWeightChangeSum

"""
A function to compute a weight change for a given Kohonen unit and data point.
"""
def get_weight_change(unit, dataPoint):
    unitCoordinates = deepcopy(unit.get_coordinates())
    weightChange = Vector(unitCoordinates)
    multiplier = -1
    weightChange.multiply_by(multiplier)
    weightChange.add(dataPoint)
    
    learningRate = 0.1
    weightChange.multiply_by(learningRate)
    return weightChange

"""
A function to compute a weight change sum for a given weight change.
"""
def get_weight_change_sum(weightChange):
    weightChangeCoordinates = weightChange.get_coordinates()
    weightChangeSum = 0

    for coordinate in weightChangeCoordinates:
        weightChangeSum += abs(coordinate)

    return weightChangeSum

"""
A function to print weight change sums in epochs.
"""
def print_epoch_weight_change_sums(epochWeightChangeSums):
    for epochWeightChangeSum in epochWeightChangeSums:
        output = str(epochWeightChangeSum)
        print(output)

"""
A function to cluster given data points into given Kohonen units.
"""
def cluster(dataPoints, units):
    print("Data point clusters:")
    dataPointClusters = get_data_point_clusters(dataPoints, units)
    keys = dataPointClusters.keys()

    for key in keys:
        output = "Cluster " + str(key) + ":"
        print(output)

        output = "Data points:"
        print(output)
        dataPointCluster = dataPointClusters[key]
        print_data_point_cluster(dataPointCluster)

"""
A function to get data point clusters for given data points and Kohonen units.
"""
def get_data_point_clusters(dataPoints, units):
    dataPointClusters = {}

    for dataPoint in dataPoints:
        unit = get_nearest_unit(dataPoint, units)
        unitIsInDataPointClusters = unit in dataPointClusters

        if unitIsInDataPointClusters:
            dataPointClusters[unit].append(str(dataPoint))
        else:
            dataPointClusters[unit] = [str(dataPoint)]

    return dataPointClusters

def print_data_point_cluster(dataPointCluster):
    for dataPoint in dataPointCluster:
        output = str(dataPoint)
        print(output)

"""
A function to get the nearest of given Kohonen units to a given data point.
"""
def get_nearest_unit(dataPoint, units):
    nets = get_nets(dataPoint, units)        
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
A function to compute given Kohonen units' nets using a given data point.
"""
def get_nets(dataPoint, units):
    nets = []

    for unit in units:
        net = get_net(dataPoint, unit)
        nets.append(net)

    return nets

"""
A function to compute a given Kohonen unit's net using a given data point.
"""
def get_net(dataPoint, unit):
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

    return net

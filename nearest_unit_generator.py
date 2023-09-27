"""
A module to get the nearest of given Kohonen units to a given data point.
"""

from vector import *

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

from vector import *

def train(dataPoints, units):
    for dataPoint in dataPoints:
        dataPoint.normalise()

    for unit in units:
        unit.normalise()

    done = False
    epoch = 1
    sigmas_epoch = []

    while not done:
        print("Epoch " + str(epoch))
        print("Iteration weight changes:")
        sigma_epoch = 0
        
        #choose training example (sequentially)
        for i in range(0, len(dataPoints)):
            unit = get_nearest_unit(dataPoints[i], units)
            #deep copy
            delta = Vector(unit.get_coordinates()[:])
            delta.multiply_by(-1)
            delta.add(dataPoint)
            #learning rate
            delta.multiply_by(0.1)
            sigma_iteration = 0

            for coordinate in delta.get_coordinates():
                sigma_iteration += abs(coordinate)

            print(sigma_iteration)
            sigma_epoch += sigma_iteration
            unit.add(delta)
            unit.normalise()

            #minimum weight change
            if sigma_iteration < .01:
                done = True
                break

        sigmas_epoch.append(sigma_epoch)
        epoch += 1

    print("Epoch weight changes:")

    for sigma_epoch in sigmas_epoch:
        print(sigma_epoch)

def get_nearest_unit(dataPoint, units):
    nets = []

    for unit in units:
        net = 0
        
        for i in range(0, len(unit.get_coordinates())):
            net += (dataPoint.get_coordinates()[i] * unit.get_coordinates()[i])

        nets.append(net)
        
    maxNet = max(nets)

    for i in range(0, len(units)):
        if nets[i] == maxNet:
            return units[i]

    return None

def cluster(dataPoints, units):
    print("Data point clusters:")
    dataPointClusters = {}

    for dataPoint in dataPoints:
        unit = get_nearest_unit(dataPoint, units)

        if unit in dataPointClusters:
            dataPointClusters[unit].append(str(dataPoint))
        else:
            dataPointClusters[unit] = [str(dataPoint)]

    for key in dataPointClusters.keys():
        print("Cluster " + str(key) + ":")
        print("Data points:")

        for dataPoint in dataPointClusters[key]:
            print(str(dataPoint))

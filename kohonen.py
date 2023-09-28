"""
A module that is an implementation of the Kohonen layer
of a Kohonen-Grossberg _counter-propagation network,
responsible for training it
and clustering the data points received from the main module.
"""
from vector import *
from copy import *

"""
A function to train a Kohonen network with given Kohonen units
by inputting given data points into the network.
"""
def train(data_points, units):
    normalise_vectors(data_points)
    normalise_vectors(units)
    epoch_weight_change_sums = get_epoch_weight_change_sums(data_points, units);

    output = "Epoch weight changes:"
    print(output)
    print_epoch_weight_change_sums(epoch_weight_change_sums)

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
def get_epoch_weight_change_sums(data_points, units):
    globals()['network_is_trained'] = False
    epoch = 1
    epoch_weight_change_sums = []

    while not globals()['network_is_trained']:
        output = "Epoch " + str(epoch)
        print(output)
        
        output = "Iteration weight changes:"
        print(output)
        
        epoch_weight_change_sum = get_epoch_weight_change_sum(data_points,
            units)
        epoch_weight_change_sums.append(epoch_weight_change_sum)
        epoch += 1

    return epoch_weight_change_sums

"""
A function to compute a weight change sum in an epoch
for given data points and Kohonen units.
"""
def get_epoch_weight_change_sum(data_points, units):
    epoch_weight_change_sum = 0
    start = 0
    data_point_count = len(data_points)
    
    #choose training example (sequentially)
    for i in range(start, data_point_count):
        data_point = data_points[i]
        unit = get_nearest_unit(data_point, units)
        weight_change = get_weight_change(unit, data_point)            
        iteration_weight_change_sum = get_weight_change_sum(weight_change)
        output = str(iteration_weight_change_sum)
        print(output)

        epoch_weight_change_sum += iteration_weight_change_sum
        unit.add(weight_change)
        unit.normalise()
        
        min_weight_change = .01
        iteration_weight_change_sum_is_negligible = iteration_weight_change_sum < min_weight_change

        if iteration_weight_change_sum_is_negligible:
            globals()['network_is_trained'] = True
            break

    return epoch_weight_change_sum

"""
A function to compute a weight change for a given Kohonen unit and data point.
"""
def get_weight_change(unit, data_point):
    unit_coordinates = deepcopy(unit.get_coordinates())
    weight_change = Vector(unit_coordinates)
    multiplier = -1
    weight_change.multiply_by(multiplier)
    weight_change.add(data_point)
    
    learning_rate = 0.1
    weight_change.multiply_by(learning_rate)
    return weight_change

def test_get_weight_change():
    x = y = z = -1
    coordinates = [x, y, z]
    unit = Vector(coordinates)

    x = y = z = -0.5
    coordinates = [x, y, z]
    data_point = Vector(coordinates)

    weight_change = get_weight_change(unit, data_point)
    coordinates = weight_change.get_coordinates()
    expected = 0.05

    for coordinate in coordinates:
        assert coordinate == expected

"""
A function to compute a weight change sum for a given weight change.
"""
def get_weight_change_sum(weight_change):
    coordinates = weight_change.get_coordinates()
    weight_change_sum = 0

    for coordinate in coordinates:
        weight_change_sum += abs(coordinate)

    return weight_change_sum

def test_get_weight_change_sum():
    x = 1
    y = 0
    z = -1
    coordinates = [x, y, z]
    weight_change = Vector(coordinates)
    weight_change_sum = get_weight_change_sum(weight_change)
    expected = 2
    assert weight_change_sum == expected

"""
A function to print weight change sums in epochs.
"""
def print_epoch_weight_change_sums(epoch_weight_change_sums):
    for epoch_weight_change_sum in epoch_weight_change_sums:
        output = str(epoch_weight_change_sum)
        print(output)

"""
A function to cluster given data points into given Kohonen units.
"""
def cluster(data_points, units):
    print("Data point clusters:")
    data_point_clusters = get_data_point_clusters(data_points, units)
    keys = data_point_clusters.keys()

    for key in keys:
        output = "Cluster " + str(key) + ":"
        print(output)

        output = "Data points:"
        print(output)
        data_point_cluster = data_point_clusters[key]
        print_data_point_cluster(data_point_cluster)

"""
A function to get data point clusters for given data points and Kohonen units.
"""
def get_data_point_clusters(data_points, units):
    data_point_clusters = {}

    for data_point in data_points:
        unit = get_nearest_unit(data_point, units)
        unit_is_in_data_point_clusters = unit in data_point_clusters

        if unit_is_in_data_point_clusters:
            data_point_clusters[unit].append(data_point)
        else:
            data_point_clusters[unit] = [data_point]

    return data_point_clusters

def print_data_point_cluster(data_point_cluster):
    for data_point in data_point_cluster:
        output = str(data_point)
        print(output)

"""
A function to get the nearest of given Kohonen units to a given data point.
"""
def get_nearest_unit(data_point, units):
    nets = get_nets(data_point, units)        
    max_net = max(nets)
    
    start = 0
    unit_count = len(units)

    for i in range(start, unit_count):
        net = nets[i]
        net_is_max_net = net == max_net
        
        if net_is_max_net:
            unit = units[i]
            return unit

    return None

def test_get_nearest_unit():
    x = y = z = 0
    coordinates = [x, y, z]
    data_point = expected = Vector(coordinates)
    
    start = 0
    stop = 2
    units = []

    for i in range(start, stop):
        x = y = z = i
        coordinates = [x, y, z]
        unit = Vector(coordinates)
        units.append(unit)

    nearest_unit = get_nearest_unit(data_point, units)
    nearest_unit_coordinates = nearest_unit.get_coordinates()
    expected_coordinates = expected.get_coordinates()
    stop = len(nearest_unit_coordinates)

    for i in range(start, stop):
        nearest_unit_coordinate = nearest_unit_coordinates[i]
        expected_coordinate = expected_coordinates[i]
        assert nearest_unit_coordinate == expected_coordinate

"""
A function to compute given Kohonen units' nets using a given data point.
"""
def get_nets(data_point, units):
    nets = []

    for unit in units:
        net = get_net(data_point, unit)
        nets.append(net)

    return nets

def test_get_nets():
    x = y = z = 1
    coordinates = [x, y, z]
    data_point = Vector(coordinates)

    start = 0
    stop = 2
    units = []

    for i in range(start, stop):
        x = y = z = i
        coordinates = [x, y, z]
        unit = Vector(coordinates)
        units.append(unit)

    nets = get_nets(data_point, units)

    for i in range(start, stop):
        unit = units[i]
        coordinates = unit.get_coordinates()
        expected = 0

        for coordinate in coordinates:
            expected += coordinate

        net = nets[i]
        assert net == expected

"""
A function to compute a given Kohonen unit's net using a given data point.
"""
def get_net(data_point, unit):
    net = 0
    start = 0
    unit_dimensionality = len(unit.get_coordinates())
    
    for i in range(start, unit_dimensionality):
        data_point_coordinates = data_point.get_coordinates()
        data_point_coordinate = data_point_coordinates[i]

        unit_coordinates = unit.get_coordinates()
        unit_coordinate = unit_coordinates[i]
        
        product = data_point_coordinate * unit_coordinate
        net += product

    return net

def test_get_net():
    x = y = z = 1
    coordinates = [x, y, z]
    data_point = unit = Vector(coordinates)
    net = get_net(data_point, unit)
    expected = 3
    assert net == expected

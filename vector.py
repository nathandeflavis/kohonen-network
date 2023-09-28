"""
A class representing an n-dimensional vector,
responsible for computing its length,
and normalising and performing arithmetic on it.
"""
from math import *

class Vector:
    """
    A function to initialise this vector with given coordinates.
    """
    def __init__(self, coordinates):
        self._coordinates = coordinates

    def test_init():
        x = y = z = 1
        expected_coordinates = [x, y, z]
        vector = Vector(expected_coordinates)
        actual_coordinates = vector.get_coordinates()
        start = 0
        stop = len(expected_coordinates)

        for i in range(start, stop):
            expected_coordinate = expected_coordinates[i]
            actual_coordinate = actual_coordinates[i]
            assert actual_coordinate == expected_coordinate

    """
    A function to represent this vector as a string.
    """
    def __str__(self):
        coordinates = self._coordinates
        coordinate_strings = []

        for coordinate in coordinates:
            coordinate_string = str(coordinate)
            coordinate_strings.append(coordinate_string)
        
        delimiter = ", "
        s = "(" + delimiter.join(coordinate_strings) + ")"
        return s

    def test_str():
        x = y = z = 1
        coordinates = [x, y, z]
        coordinate_strings = []

        for coordinate in coordinates:
            coordinate_string = str(coordinate)
            coordinate_strings.append(coordinate_string)
        
        delimiter = ", "
        expected = "(" + delimiter.join(coordinate_strings) + ")"

        vector = Vector(coordinates)
        actual = str(vector)
        assert actual == expected

    """
    A getter function for this vector's coordinates.
    """
    def get_coordinates(self):
        coordinates = self._coordinates
        return coordinates

    """
    A function to compute this vector's length
    as the square root of the sum of its squared coordinates.
    """
    def get_length(self):
        square_sum = 0.0
        coordinates = self._coordinates
        power = 2

        for coordinate in coordinates:
            square = coordinate ** power
            square_sum += square

        length = sqrt(square_sum)
        return length

    def test_get_length():
        x = 0
        y = 3
        z = 4
        coordinates = [x, y, z]
        vector = Vector(coordinates)
        expected = 5
        actual = vector.get_length()
        assert actual == expected

    """
    A function to normalise this vector
    such that its coordinates are in the interval [0, 1].
    """
    def normalise(self):
        length = self.get_length()
        coordinates = self._coordinates
        start = 0
        stop = len(coordinates)

        for i in range(start, stop):
            coordinate = coordinates[i]
            coordinate /= length
            coordinates[i] = coordinate

    def test_normalise():
        x = 0
        y = 3
        z = 4
        coordinates = [x, y, z]
        vector = Vector(coordinates)
        vector.normalise()
        expected_coordinates = []
        length = vector.get_length()

        for coordinate in coordinates:
            expected_coordinate = coordinate / length
            expected_coordinates.append(expected_coordinate)

        actual_coordinates = vector.get_coordinates()
        start = 0
        stop = len(expected_coordinates)

        for i in range(start, stop):
            expected_coordinate = expected_coordinates[i]
            actual_coordinate = actual_coordinates[i]
            assert actual_coordinate == expected_coordinate
        

    """
    A function to add the coordinates of that given vector
    to the coordinates of this vector.
    """
    def add(self, vector):
        this_coordinates = self._coordinates
        that_coordinates = vector._coordinates
        start = 0
        stop = len(this_coordinates)
        
        for i in range(start, stop):
            this_coordinate = this_coordinates[i]
            that_coordinate = that_coordinates[i]
            this_coordinate += that_coordinate
            this_coordinates[i] = this_coordinate

    def test_add():
        x = y = z = 1
        coordinates = [x, y, z]
        vector = Vector(coordinates)
        vector.add(vector)
        coordinates = vector.get_coordinates()
        expected = 2

        for coordinate in coordinates:
            assert coordinate == expected

    """
    A function to multiply this vector's coordinates by a given multiplier.
    """
    def multiply_by(self, multiplier):
        coordinates = self._coordinates
        start = 0
        stop = len(coordinates)
        
        for i in range(start, stop):
            coordinate = coordinates[i]
            coordinate *= multiplier
            coordinates[i] = coordinate

    def test_multiply_by():
        x = y = z = 1
        coordinates = [x, y, z]
        vector = Vector(coordinates)
        multiplier = 2
        vector.multiply_by(multiplier)
        coordinates = vector.get_coordinates()

        for coordinate in coordinates:
            assert coordinate == multiplier

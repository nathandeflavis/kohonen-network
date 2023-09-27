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

    """
    A function to represent this vector as a string.
    """
    def __str__(self):
        coordinates = self._coordinates
        coordinateStrings = []

        for coordinate in coordinates:
            coordinateString = str(coordinate)
            coordinateStrings.append(coordinateString)
        
        delimiter = ", "
        s = "(" + delimiter.join(coordinateStrings) + ")"
        return s

    """
    A getter function for this vector's coordinates.
    """
    def get_coordinates(self):
        coordinates = self._coordinates
        return coordinates

    """
    A function to get this vector's length
    as the square root of the sum of its squared coordinates.
    """
    def get_length(self):
        squareSum = 0.0
        coordinates = self._coordinates
        power = 2

        for coordinate in coordinates:
            square = coordinate ** power
            squareSum += square

        length = sqrt(squareSum)
        return length

    """
    A function to normalise this vector
    such that its coordinates are in the interval [0, 1].
    """
    def normalise(self):
        length = self.get_length()
        coordinates = self._coordinates
        start = 0
        dimensionality = len(coordinates)

        for i in range(start, dimensionality):
            coordinate = coordinates[i]
            coordinate /= length
            coordinates[i] = coordinate

    """
    A function to add the coordinates of that given vector
    to the coordinates of this vector.
    """
    def add(self, vector):
        thisCoordinates = self._coordinates
        thatCoordinates = vector._coordinates
        start = 0
        thisDimensionality = len(thisCoordinates)
        
        for i in range(start, thisDimensionality):
            thisCoordinate = thisCoordinates[i]
            thatCoordinate = thatCoordinates[i]
            thisCoordinate += thatCoordinate
            thisCoordinates[i] = thisCoordinate

    """
    A function to multiply this vector's coordinates by a given multiplier.
    """
    def multiply_by(self, multiplier):
        coordinates = self._coordinates
        start = 0
        dimensionality = len(coordinates)
        
        for i in range(start, dimensionality):
            coordinate = coordinates[i]
            coordinate *= multiplier
            coordinates[i] = coordinate

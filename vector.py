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
        s = "(" + str(self._coordinates[0])

        for i in range(1, len(self._coordinates)):
            s += ", " + str(self._coordinates[i])

        s += ")"
        return s       

    """
    A getter function for this vector's coordinates.
    """
    def get_coordinates(self):
        return self._coordinates

    """
    A function to get this vector's length
    as the square root of the sum of its squared coordinates.
    """
    def get_length(self):
        squareSum = 0.0

        for coordinate in self._coordinates:
            squareSum = squareSum + coordinate ** 2

        return sqrt(squareSum)

    """
    A function to normalise this vector
    such that its coordinates are in the interval [0, 1].
    """
    def normalise(self):
        length = self.get_length()
        coordinates = self._coordinates

        for i in range(0, len(coordinates)):
            coordinates[i] /= length

    """
    A function to add the coordinates of a given other vector
    to the coordinates of this vector.
    
    """
    def add(self, vector):
        myCoordinates = self._coordinates
        
        for i in range(0, len(myCoordinates)):
            myCoordinates[i] += vector._coordinates[i]

    """
    A function to multiply this vector's coordinates by a given multiplier.
    """
    def multiply_by(self, multiplier):
        coordinates = self._coordinates
        
        for i in range(0, len(coordinates)):
            coordinates[i] *= multiplier

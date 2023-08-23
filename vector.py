from math import *

class Vector:
    def __init__(self, coordinates):
        self._coordinates = coordinates

    def __str__(self):
        s = "(" + str(self._coordinates[0])

        for i in range(1, len(self._coordinates)):
            s += ", " + str(self._coordinates[i])

        s += ")"
        return s       

    def get_coordinates(self):
        return self._coordinates
    
    def get_length(self):
        squareSum = 0.0

        for coordinate in self._coordinates:
            squareSum = squareSum + coordinate ** 2

        return sqrt(squareSum)

    def normalise(self):
        length = self.get_length()
        coordinates = self._coordinates

        for i in range(0, len(coordinates)):
            coordinates[i] /= length

    def add(self, vector):
        myCoordinates = self._coordinates
        
        for i in range(0, len(myCoordinates)):
            myCoordinates[i] += vector._coordinates[i]

    def multiply_by(self, multiplier):
        coordinates = self._coordinates
        
        for i in range(0, len(coordinates)):
            coordinates[i] *= multiplier

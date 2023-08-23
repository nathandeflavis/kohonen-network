# kohonen-network
A Kohonen network that supports 2 to 4 3D units

I programmatically implemented a Kohonen network that supported 2 to 4 units, each of which was 3-dimensional.

The entry point to the program is the main() function in the __main__module. The interaction between the user and the program is command-line-style. The program consists of 3 modules:
- **__main__**. The entry point into the program, responsible for getting user input and passing data points to the 'kohonen' module.
- **kohonen**. An implementation of the Kohonen layer of a Kohonen-Grossberg counter-propagation network, responsible for training it and clustering the data points received from the main module.
- **vector**. A class representing an n-dimensional vector, responsible for computing its length, and normalising and performing arithmetic on it.

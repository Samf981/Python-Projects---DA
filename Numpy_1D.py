import numpy as np 

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])

# Check the type of the array
type(a)

# Check the type of the values stored in numpy array
a.dtype

# Assign the third element to 100
c = np.array([20, 1, 2, 3, 4])
c[2] = 100

# Slicing the numpy array
d = c[1:4]

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400

# Get the size of numpy array
a.size

# Get the number of dimensions of numpy array
a.ndim

# Get the shape/size of numpy array
print(a.shape)

# Get the mean of numpy array
a.mean()

# Get the standard deviation of numpy array
standard_deviation=a.std()

# Get the biggest and samllest value in the numpy array

max_b = a.max()
min_b=a.min()
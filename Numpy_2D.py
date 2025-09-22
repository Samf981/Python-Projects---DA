import numpy as np
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

# Convert list to Numpy Array
A = np.array(a)

# Show the numpy array dimensions, shape, size
A.ndim
A.shape
A.size

# Access the element on the second row and third column
A[1, 2]

# Access the element on the first and second rows and third column
A[0:2, 2]

# Add X and Y, substract, multiply
X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 
Z = X + Y
Z = X - Y
Z = X * Y

#Calculate the Dot Product
Z = np.dot(X,Y)
import numpy as np


# # MODE
# speed = [99,86,87,88,86,103,87,94,78,77,85,86]
# x = numpy.median(speed)
# print(x)
# # = 86 Most common    


# # MEDIAN
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# x = numpy.median(speed)
# print(x)
# # after sort list given the centreer number of list if in center tow numbers is returned (86 + 87) / 2 = 86.5


## MEAN
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# x = numpy.mean(speed)
# print(x)
## it returned averge number of liste soo ((99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77)

# NumPy routines which allocate memory and fill with user specified values
a = np.array([5,4,3,2, 6]);  print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}")
a = np.array([5.,4,3,2]); print(f"np.array([5.,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
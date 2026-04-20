# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = np.array([390, 580, 690, 910, 1280, 1550, 553, 336, 778, 888])

# x_norm = x / 15
# y_norm = y / 2000

# w = 0
# b = 0


# def compute_cost(x, y, w, b):
#     m = len(x)
#     total = 0
#     for i in range(m):
#         prediction = w * x[i] + b
#         error = prediction - y[i]
#         total += error**2
#     return total / (2 * m)


# def compute_gradient(x, y, w, b):
#     m = len(x)
#     dj_dw = 0
#     dj_db = 0

#     for i in range(m):
#         prediction = w * x[i] + b
#         error = prediction - y[i]

#         dj_dw += error * x[i]
#         dj_db += error

#     return dj_dw / m, dj_db / m


# alpha = 0.1
# iterations = 1000

# for i in range(iterations):
#     dj_dw, dj_db = compute_gradient(x_norm, y_norm, w, b)

#     w = w - alpha * dj_dw
#     b = b - alpha * dj_db

#     if i % 100 == 0:
#         cost = compute_cost(x_norm, y_norm, w, b)
#         print(f"iteration {i}: cost={cost:.5f}")

# print("\nFinal w, b (normalized):", w, b)


# plt.scatter(x_norm, y_norm, color='red', label='Data')

# x_line = np.linspace(0, 1, 100)
# y_line = w * x_line + b

# plt.plot(x_line, y_line, color='blue', label='Regression Line')

# plt.legend()
# plt.title("Linear Regression (Normalized)")
# plt.show()







# import numpy as np
# import matplotlib.pyplot as plt

# # data
# x = np.array([1,2,3,4,5,6,7,8,9,10])
# y = np.array([390,580,690,910,1280,1550,553,336,778,888])

# # normalize
# x = x / 15
# y = y / 2000

# # params
# w, b = 0, 0

# # settings
# alpha = 0.1
# iterations = 1000
# m = len(x)

# for i in range(iterations):
#     predictions = w * x + b
#     errors = predictions - y

#     # gradient
#     dw = np.dot(errors, x) / m
#     db = np.sum(errors) / m

#     # update
#     w -= alpha * dw
#     b -= alpha * db

#     if i % 100 == 0:
#         cost = np.sum(errors**2) / (2*m)
#         print(f"iteration {i}: cost={cost:.5f}")

# print("\nFinal w, b:", w, b)

# # plot
# plt.scatter(x, y, color='red')
# plt.plot(x, w*x + b, color='blue')
# plt.show()


# import sys
# import matplotlib

# import matplotlib.pyplot as plt
# from scipy import stats

# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x):
#     return slope * x + intercept

# mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()


import numpy
import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

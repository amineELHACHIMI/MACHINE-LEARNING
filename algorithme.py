import numpy as np
import matplotlib.pyplot as plt


x = []
y = []

for i in range(50):
    xi = np.random.randint(0, 100)
    noise = np.random.randint(-1000, 1000)

    yi = 50 * xi + 200 + noise

    x.append(xi)
    y.append(yi)

x = np.array(x)
y = np.array(y)

x = x / np.max(x)
y = y / np.max(y)

w, b = 0, 0

alpha = 0.1
iterations = 10000
m = len(x)

for i in range(iterations):
    predictions = w * x + b
    errors = predictions - y

    dw = np.dot(errors, x) / m
    db = np.sum(errors) / m

    w -= alpha * dw
    b -= alpha * db

    if i % 100 == 0:
        cost = np.sum(errors**2) / (2*m)
        print(f"iteration {i}: cost={cost:.5f}")

print("\nFinal w, b:", w, b)

plt.scatter(x, y, color='red')
plt.plot(x, w*x + b, color='blue')
plt.show()

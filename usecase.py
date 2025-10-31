import numpy as np
import matplotlib.pyplot as plt
import math

# ----------------------------
# 1. Uniform Distribution
# ----------------------------
x1 = np.linspace(0, 1, 200)
y1 = np.ones_like(x1)  # pdf = 1 on [0,1]

plt.figure(figsize=(8, 4))
plt.plot(x1, y1, label='Uniform(0,1)')
plt.title("Uniform Probability Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()

# ----------------------------
# 2. Binomial Distribution
# ----------------------------
def binom_pmf(k, n, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

n, p = 10, 0.5
x2 = np.arange(n + 1)
y2 = np.array([binom_pmf(k, n, p) for k in x2])

plt.figure(figsize=(8, 4))
plt.stem(x2, y2, use_line_collection=True)
plt.title(f"Binomial(n={n}, p={p}) Probability Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid(True)
plt.show()

# ----------------------------
# 3. Normal Distribution
# ----------------------------
def normal_pdf(x, mu=0, sigma=1):
    coef = 1.0 / (math.sqrt(2 * math.pi) * sigma)
    exp = np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    return coef * exp

x3 = np.linspace(-4, 4, 400)
y3 = normal_pdf(x3, mu=0, sigma=1)

plt.figure(figsize=(8, 4))
plt.plot(x3, y3, label='N(0,1)')
plt.title("Normal Probability Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()

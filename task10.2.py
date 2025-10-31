import matplotlib.pyplot as plt

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
visitors = [120, 150, 180, 90, 200, 300, 250]

plt.plot(days, visitors, marker='o', linestyle='-', color='blue')

plt.xlabel("Days of the Week")
plt.ylabel("Number of Visitors")
plt.title("Website Traffic Over a Week")
plt.grid(True)

plt.show()

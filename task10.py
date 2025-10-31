import matplotlib.pyplot as plt

students = ["alice", "bob", "charlie", "david", "eve"]
math = [85, 70, 90, 60, 75]
science = [78, 88, 95, 67, 80]
english = [82, 76, 88, 72, 84]

x = range(len(students))

# Bars for each subject
plt.bar(x, math, width=0.25, label="Math")
plt.bar([i + 0.25 for i in x], science, width=0.25, label="Science")
plt.bar([i + 0.50 for i in x], english, width=0.25, label="English")

# Labels and title
plt.xticks([i + 0.25 for i in x], students)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks Comparison")
plt.legend()
plt.show()

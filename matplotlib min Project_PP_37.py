import matplotlib.pyplot as plt

# Sample data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
grades = [85, 92, 78, 90, 88]

# Plotting the bar chart
plt.figure(figsize=(8, 5))
plt.bar(students, grades, color='skyblue')

# Adding title and labels
plt.title('Student Grades')
plt.xlabel('Students')
plt.ylabel('Grades')

# Adding grade labels on top of bars
for i, grade in enumerate(grades):
    plt.text(i, grade + 1, str(grade), ha='center')

# Show the plot
plt.tight_layout()
plt.show()

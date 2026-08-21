# File Handling Operations - Part 1

file = open("student.txt", "w")

file.write("My name is Rahul.\n")
file.write("I am learning Python.\n")
file.write("Python is easy to learn.\n")
file.write("File handling is an important topic.\n")

file.close()

print("File created successfully!")

file = open("student.txt", "r")

print("\nFile Content:")
print(file.read())

file.close()
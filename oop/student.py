import matplotlib.pyplot as py
import numpy as np
students =["Arun","Bina","chetan","Divya","Esha"]
marks = [75,85,90,70,95]
py.plot(students,marks)
py.show()
py.bar(students,marks)
py.xlabel(students)
py.ylabel(marks)
py.show()
py.scatter(students,marks)
py.show()


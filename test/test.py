def convert(degrees):
    return((degrees*3.14)/180)
degrees = 150
radians = convert(degrees)
print("Degrees:", degrees)
print("Radians:", radians)


student1 = 90.0
student2 = 80.0
student3 = 66.5
average = ((student1 + student2 + student3)/3)
print("Student scores: ")
print(student1)
print(student2)
print(student3)
print("Average: ", average)

class_1 = 32
class_2 = 45
class_3 = 51
groups1, groups2, groups3 = (class_1 // 5), (class_2 // 7), (class_3 // 6)
left1, left2, left3 = (class_1 % 5), (class_2 % 7), (class_3 % 6)
print("Number of students in each group:")
print(groups1)
print(groups2)
print(groups3)
print("Number of students leftover:")
print(left1)
print(left2)
print(left3)

pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter / 2
circumference = 2 * pi * pie_radius
circumference_msg = "Jimmy’s pie has a circumference: "
print(circumference_msg, circumference)

velocity = 343
frequency = 256
calculation = (velocity/frequency)
print("The speed (m/s) =",velocity )
print("The frequency (Hz) =", frequency)
print("the wavelength (m) =", calculation)
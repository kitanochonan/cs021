#CS021
#Module2 Calculate and display the sphere diameter, circumference, surface area and volume

#Constant PI
PI = 3.14

#Prompt user for the radius of a sphere
radius = float(input("Enter the radius: "))

#Calculate and print the diameter
diameter = radius * 2
print("Diameter:", format(diameter, ".1f"))

#Calculate and print the circumference
circumference = diameter * PI
print("Circumference:", format(circumference, ".1f"))

#Calculate and print the surface area
surface_area = radius ** 2 * 4 * PI
print("Surface area:", format(surface_area, ".1f"))

#Calculate and print the volume
volume = radius ** 3 * PI * 4 / 3
print("Volume:", format(volume, ".1f"))

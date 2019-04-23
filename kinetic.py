# CS21
# A program which calculates Kinetic Energy
# KE = mass * velocity ** 2 / 2

def main():
    # Ask user for object's mass and velocity
    try:
        mass = float(input("Object's mass in kilograms?: "))
        velocity = float(input("Object's velocity (mps)?: "))
    except ValueError:
        print("Invalid input")

    try:
        # Give mass and velocity to kinetic_energy() function
        print("Kenetic Energy is:", format(kinetic_energy(mass, velocity), ".2f"))
    except UnboundLocalError:
        print("Could not calculate Kenetic Energy.")

def kinetic_energy(mass, velocity):
    # Calculation of Kenetic Energy
    KE = mass * velocity**2 / 2
    return KE

main()

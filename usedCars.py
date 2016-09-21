"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from car import Car


def main():

    bus = Car(180, 'bus')
    bus.add_fuel(20)
    bus.drive(30)
    print(bus)

    limo = Car(120, "limo")
    limo.drive(115)
    print(limo)




main()
from guitar import Guitar


def main():
    guitars = []
    name = 'valid'
    while name != "":
        name = input("enter guitar name ").strip()
        if name == "":
            break
        year = int(input("enter year made "))
        cost = float(input("enter cost of guitar "))

        new_guitar = print(Guitar(name, year, cost))
        guitars.append(new_guitar)

    print("These are my guitars:")
    guitar_count = 0
    #TODO vintage
    for guitar in guitars:
        print("The age of this guitar is: " + str(guitar.get_age())+ "years")
        guitar_count += 1


main()
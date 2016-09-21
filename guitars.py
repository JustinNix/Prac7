from guitar import Guitar


def main():
    name = 'valid'
    while name != "":
        name = input("enter guitar name ").strip()
        if name == "":
            break
        year = int(input("enter year made "))
        cost = float(input("enter cost of guitar "))


        new_guitar = Guitar(name, year, cost)
        guitars = [new_guitar]
        print(new_guitar)

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar.is_vintage())



main()

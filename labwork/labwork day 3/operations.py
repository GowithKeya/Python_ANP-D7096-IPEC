import twodfigures


def get_positive_number(prompt):
    while True:
        value = float(input(prompt))
        if value > 0:
            return value
        print("Please enter a positive value.")


while True:
    print("\n--- Geometry Calculator ---")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    figure_choice = input("Enter your choice (1-5): ")

    if figure_choice == "5":
        print("Exiting Geometry Calculator.")
        break

    if figure_choice not in {"1", "2", "3", "4"}:
        print("Invalid figure choice. Please try again.")
        continue

    print("\nSelect operation:")
    print("1. Area")
    print("2. Perimeter")
    operation_choice = input("Enter operation choice (1-2): ")

    if operation_choice not in {"1", "2"}:
        print("Invalid operation choice. Please try again.")
        continue

    if figure_choice == "1":
        side = get_positive_number("Enter side of square: ")
        if operation_choice == "1":
            result = twodfigures.square_area(side)
            print(f"Area of square: {result:.2f}")
        else:
            result = twodfigures.square_perimeter(side)
            print(f"Perimeter of square: {result:.2f}")

    elif figure_choice == "2":
        radius = get_positive_number("Enter radius of circle: ")
        if operation_choice == "1":
            result = twodfigures.circle_area(radius)
            print(f"Area of circle: {result:.2f}")
        else:
            result = twodfigures.circle_perimeter(radius)
            print(f"Circumference of circle: {result:.2f}")

    elif figure_choice == "3":
        if operation_choice == "1":
            base = get_positive_number("Enter base of triangle: ")
            height = get_positive_number("Enter height of triangle: ")
            result = twodfigures.triangle_area(base, height)
            print(f"Area of triangle: {result:.2f}")
        else:
            side1 = get_positive_number("Enter side 1 of triangle: ")
            side2 = get_positive_number("Enter side 2 of triangle: ")
            side3 = get_positive_number("Enter side 3 of triangle: ")
            result = twodfigures.triangle_perimeter(side1, side2, side3)
            print(f"Perimeter of triangle: {result:.2f}")

    elif figure_choice == "4":
        length = get_positive_number("Enter length of rectangle: ")
        breadth = get_positive_number("Enter breadth of rectangle: ")
        if operation_choice == "1":
            result = twodfigures.rectangle_area(length, breadth)
            print(f"Area of rectangle: {result:.2f}")
        else:
            result = twodfigures.rectangle_perimeter(length, breadth)
            print(f"Perimeter of rectangle: {result:.2f}")

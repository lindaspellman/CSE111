import math 

def main():
    circles = []
    radius = ""

    try:
        while radius != "end":
            print("Answer 'end' when you're finished.")
            radius = input("Radius: ")
            if radius == "end":
                pass
            else:
                radius = float(radius)
                circles.append(calculate_circle_area(radius))

        print(circles)
    
    except ValueError as val_err:
        print(f"ValueError: '{val_err}' is not a valid float")
        main()
    

def calculate_circle_area(radius):
    area = math.pi * radius**2

    return area

main()
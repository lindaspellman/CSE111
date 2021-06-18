import math


def main():
    with open("cans.txt") as cans: 
        next(cans)
        best_stor_eff = 0
        for line in cans:
            line = line.split(",")
            name = line[0]
            radius = float(line[1])
            height = float(line[2])
            cost = line[3]
            # print(f"{name}, {radius}, {height}, {cost}")
            storage = storage_efficiency(radius, height)
            print(f"{name} {storage:.1f}")
            if storage > best_stor_eff:
                best_stor_eff = storage
                name_best = name 
        print(f"Best Storage Efficiency: {name_best}, {best_stor_eff:.1f}")
            

def cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def storage_efficiency(radius, height):
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency


# Call main() to start the program
main()
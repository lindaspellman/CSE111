import math
 
def main(): ## program driver - GOAL: Keep lean
 ## prompt user for how many circles they have
 numberOfCircles = int(input("How many circles are we working with? "))
 areasList = loopForCircles(numberOfCircles)
 displayAreas(areasList)
 ## display each area: separate print statements or a list?
 
def displayAreas(areasList):
 areasList = [round(i, 2) for i in areasList]
 print(areasList)
 
def loopForCircles(numberOfCircles):
 circleAreas = []
 ## loop x times: compute area for each circle
 for _ in range(numberOfCircles):
 ## get radius for each circle
    r = float(input("Please enter the radius: "))
    circleAreas.append(computeCircleArea(r))
 return circleAreas
 
def computeCircleArea(radius): ## compute and return circle area
 return math.pi * radius**2
 
if __name__ == '__main__':
 main()
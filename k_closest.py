import heapq
import random
import math

points = []
dimensions = int(input("Enter the number of dimensions: "));
numberOfPoints = int(input("Enter the number of points: "));
closestPoints = int(input("How many points do you want to calculate? "))

for i in range(numberOfPoints):
    point = []
    for j in range(dimensions):
        point.append(random.randint(0,100))
    points.append(point)

print("\nUnsorted points are: \n")
print(*points, sep = "\n")

def kClosest(points: list[list[int]], closestPoints : int) -> list[list[int]]:
    minHeap = []
    dist = 0
    for point in points:
        for i in point:
            dist += (i**2)
        dist = round(math.sqrt(dist), 2)
        minHeap.append([dist, point])
        dist = 0
    
    minHeap = sorted(minHeap)   
    heapq.heapify(minHeap)

    print("\nSorted points are: \n")
    print(*minHeap, sep = "\n")
    print("\nClosest points are: \n")

    for i in range(0, closestPoints):
        print(minHeap[i])

kClosest(points, closestPoints)

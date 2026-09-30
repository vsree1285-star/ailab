import heapq
import math

locations = {
    "Entrance": (0, 0),
    "Reception": (2, 1),
    "Emergency": (1, 4),
    "Pharmacy": (4, 0),
    "Lab": (5, 2),
    "OPD": (4, 4),
    "Radiology": (7, 1),
    "Cardiology": (7, 4),
    "ICU": (9, 3),
    "Surgery": (10, 5),
}

graph = {
    "Entrance": ["Reception", "Emergency"],
    "Reception": ["Entrance", "Pharmacy", "OPD"],
    "Emergency": ["Entrance", "OPD"],
    "Pharmacy": ["Reception", "Lab"],
    "OPD": ["Reception", "Emergency", "Lab", "Cardiology"],
    "Lab": ["Pharmacy", "OPD", "Radiology"],
    "Radiology": ["Lab", "ICU"],
    "Cardiology": ["OPD", "ICU", "Surgery"],
    "ICU": ["Radiology", "Cardiology", "Surgery"],
    "Surgery": ["Cardiology", "ICU"],
}

def heuristic(place, goal):
    x1, y1 = locations[place]
    x2, y2 = locations[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def best_first_search(start, goal):
    open_list = [(heuristic(start, goal), start, [start])]
    visited = set()

    while open_list:
        h, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)
        print("Visiting:", current, "| h =", round(h, 2))

        if current == goal:
            return path

        for neighbour in graph[current]:
            if neighbour not in visited:
                new_h = heuristic(neighbour, goal)
                heapq.heappush(
                    open_list,
                    (new_h, neighbour, path + [neighbour])
                )

    return None


print("----- SMART HOSPITAL NAVIGATION ASSISTANT -----")
print("Available places:")

for place in locations:
    print(" -", place)

start = input("\nEnter your current location: ").strip().title()
goal = input("Enter your destination: ").strip().title()

if goal == "Opd":
    goal = "OPD"
if goal == "Icu":
    goal = "ICU"
if start == "Opd":
    start = "OPD"
if start == "Icu":
    start = "ICU"

if start not in locations or goal not in locations:
    print("Invalid location. Please choose from the available places.")
else:
    print("\n----- BEST FIRST SEARCH -----")
    path = best_first_search(start, goal)

    print("\n----- SUGGESTED ROUTE -----")

    if path:
        print(" -> ".join(path))
        print("Number of stops:", len(path) - 1)
    else:
        print("No route found.")
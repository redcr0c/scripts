def find_closest_level(levels: list[int], current_floor: int) -> int:
        if not levels:
            raise ValueError("Levels list cannot be empty!")
        return min(levels, key = lambda x: abs(x - current_floor))
    
current_floor = 5
levels = [19,2,4,6,27,21,13]
path = [current_floor]

while levels:
    closest_level = find_closest_level(levels, current_floor)
    path.append(closest_level)
    current_floor = closest_level
    levels.remove(closest_level)
    
print("The elevator moves like this:", " -> ".join(map(str,path)))

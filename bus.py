bus_stops = [[10,0],[3,5],[5,8]]
final = 0
for char in bus_stops:
    final = final + char[0] - char[1]
print(final)
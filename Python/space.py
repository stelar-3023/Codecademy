weight = int(input("Weight: "))
planet = input("Planet: ")

if planet == "Venus":
    weight = weight * 0.91
elif planet == "Mars":
    weight = weight * 0.38
elif planet == "Jupiter":
    weight = weight * 2.34
elif planet == "Saturn":
    weight = weight * 1.06
elif planet == "Uranus":
    weight = weight * 0.92
elif planet == "Neptune":
    weight = weight * 1.19
elif planet == "Earth":
    weight = weight * 1
else:
    print("Invalid Planet")

print("Your weight:", weight)

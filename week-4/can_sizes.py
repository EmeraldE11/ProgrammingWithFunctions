from math import pi

def main():
    cans = [
    {"name":"#1 Picnic",   "radius": 6.83 ,  "height": 10.16},
    {"name":"#1 Tall",     "radius": 7.78 ,  "height": 11.91},
    {"name":"#2",          "radius": 8.73 ,  "height": 11.59},
    {"name":"#2.5",        "radius": 10.32 , "height": 11.91},
    {"name":"#3 Cylinder", "radius": 10.79 , "height": 17.78},
    {"name":"#5",          "radius": 13.02 , "height": 14.29},
    {"name":"#6Z",         "radius": 5.40 ,  "height": 8.89},
    {"name":"#8Z short",   "radius": 6.83 ,  "height": 7.62},
    {"name":"#10",         "radius": 15.72 , "height": 17.78},
    {"name":"#211",        "radius": 6.83 ,  "height": 12.38},
    {"name":"#300",        "radius": 7.62 ,  "height": 11.27},
    {"name":"#303",        "radius": 8.10 ,  "height": 11.11}
    ]

    for i in range(0, 12):
        volume = cylinder_volume(cans[i]["radius"], cans[i]["height"])
        area = surface_area(cans[i]["radius"], cans[i]["height"])
        efficiency = storage_efficiency(volume, area)
        
        name = cans[i]["name"]
        print(f"{name} {efficiency:.1f}")

def cylinder_volume(radius, height):
    return pi * (radius * radius) * height

def surface_area(radius, height):
    return 2 * pi * radius * (radius + height)

def storage_efficiency(cylinder_volume, surface_area):
    return cylinder_volume/surface_area

main()
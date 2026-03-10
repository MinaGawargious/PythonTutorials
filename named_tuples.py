from collections import namedtuple
# namedtuples are lightweight objects that work like regular objects but are more readable

color = (55, 155, 255) # RGB
print("color[0] =",color[0])
color = {"red": 55, "green": 155, "blue": 255} # RGB dict. Maybe we want tuples since they are immutable and dictionaries require more typing
print("color['red'] =", color["red"])

# namedtuple:
Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(55, 155, 255)
print("color[0] =", color[0])
print("color.red =", color.red)
color = Color(red=55, green=155, blue=255)
# print(color["red"]) # illegal
age: int = 25
height: float = 180

number: complex = 4 + 5j

height = input('enter your height: ')
width = input('enter you width: ')

print('height: ', height, type(height))
print('width: ', width, type(width))

height_int: int = float(height)
width_int: int = float(width)

print(type(height_int))
print(type(width_int))

print(int(9.8))
print(int(9.8) == 10)

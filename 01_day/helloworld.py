print("Hello World!")

print(2 * 3)
print(7 - 10)
print(2**8)

print('======')

print(type(2)) # <class 'int'>
print(type(2.2)) # <class 'int'>
print(type(type("Stan"))) # <class 'type'>
print(type("Stan")) # <class 'str'>

print(type([True, False])) # <class 'list'>
print(type((1, 3))) # <class 'tuple'>
print(type({ 'some': 'thing'})) # <class 'dict'>

count = 0

while (count < 30):
    count += 1
    print(f"- Day {count}")


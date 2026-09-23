def factorial(num: int) -> int:
    if num == 0:
        return 1
    
    result: int = 1

    for i in range(1, num + 1):
        print(i)
        result = result * i

    return result

print(factorial(1), "1!")
print(factorial(5), "5!")



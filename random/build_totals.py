def build_running_totals(numbers):
    
    if len(numbers) == 0:
        return numbers

    total = 0
    new_numbers = []

    for i in range(0, len(numbers)):
        current_number = numbers[i]
        new_numbers.append(current_number + total)
        total += current_number

    return new_numbers
        
        
print(build_running_totals([3, 2, 4]))
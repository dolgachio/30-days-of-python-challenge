# your code here

def sum_intervals(start, stop, step):
    sum: int = 0
    
    for i in range(start, stop, step):
        sum += i

    return sum

def count_boosts(power, target, boost):
    required_power: int = 0
    boosted_target: int = power
    while boosted_target < target:
        boosted_target = boosted_target + boost
        required_power += 1

    return required_power

def audit_readings(readings):
    total: int = 0
    total_count: int = 0
    
    for reading in readings:
        if reading < 0:
            continue

        if reading == 0:
            break

        total += reading
        total_count += 1

    return (total, total_count)
    
result = audit_readings([7, -2, 5, 0, 20])
print(result)
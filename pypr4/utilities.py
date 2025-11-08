def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)
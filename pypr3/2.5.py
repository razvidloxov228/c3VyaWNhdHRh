def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
primes = [num for num in range(start, end + 1) if is_prime(num)]
print(f"Прості числа в діапазоні від {start} до {end}:")
print(primes)

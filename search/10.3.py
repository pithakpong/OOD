def binary_search_sqrt(num, epsilon=0.000001):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")

    low = 0.0
    high = max(1.0, num)  # Start with an upper bound of 1 or the number itself

    while high - low > epsilon:
        mid = (low + high) / 2
        square = mid * mid

        if square > num:
            high = mid
        else:
            low = mid

    return (low + high) // 2
num = int(input("simple sqrt: "))
result = binary_search_sqrt(num)
print(f"{int(result)}")

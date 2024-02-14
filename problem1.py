number = 12

sum_of_digits = lambda x: sum(int(y) for y in str(x))

print(sum_of_digits(number))

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(1,11):
    print(is_even(i))
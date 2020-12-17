# given a number, find the sum of integers of number till the sum is single digit


def single_digit_sum(number):
    addition = 0
    while number > 0:
        addition = addition + (number % 10)
        number = number // 10
    if addition not in range(0, 10):
        return single_digit_sum(addition)
    return addition


# i = int(input("Enter a number > 9: "))
i = 999999999999999999999
add = single_digit_sum(i)

print("Single digit sum of {} is {}. ".format(i, add))

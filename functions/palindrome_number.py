def palindrome_number(x):
    copy_of_x = x
    reversed = 0

    while x > 0:
        last_digit = x % 10
        reversed = reversed * 10 + last_digit
        x //= 10

    return copy_of_x == reversed

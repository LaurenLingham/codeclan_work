def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string_length):
    return len(string_length)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month_number):
    import calendar
    return calendar.month_name[month_number]

def number_to_short_month_name(month_number):
    import calendar
    return calendar.month_abbr[month_number]

def cube(num_1):
    return num_1 ** 3

def reverse_string(string):
    return string[::-1]

def celsius(temp):
    return (float(temp) - 32) / 1.8
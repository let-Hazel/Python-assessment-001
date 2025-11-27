
def cube_number(number):
    """
    1. Receive a number.
    2. Return that number raised to the power of 3.
    """
    # TODO: Write your code here
    return number ** 3
cube_number(2)

def check_even_or_odd(number):
    """
    1. Receive a number.
    2. If even, return "Even".
    3. If odd, return "Odd".
    """
    # TODO: Write your code here
    if number%2 == 0:
        return "Even"
    else:
        return "Odd"
    
check_even_or_odd(10)

def combine_names(first_name, last_name):
    """
    1. Receive two strings (first_name and last_name).
    2. Return a single string in the format: "Last, First"
    Example: combine_names("James", "Bond") -> "Bond, James"
    """
    # TODO: Write your code here
    return f"{last_name}, {first_name}"

print(combine_names("Hazel", "Sibhuku"))

def get_last_item(my_list):
    """
    1. Receive a list.
    2. Return the last item in that list (use negative indexing).
    """
    # TODO: Write your code here
    return my_list[-1]

my_list = [10, 20, 30]
get_last_item(my_list)

def sum_all_numbers(numbers):
    """
    1. Receive a list of numbers (e.g., [1, 2, 3]).
    2. Return the sum of all numbers in the list.
    Hint: You can use a 'for' loop or the built-in sum() function.
    """
    # TODO: Write your code here
    count = 0
    for i in numbers:
         count += i
    return count


numbers = [1,1,1]
sum_all_numbers(numbers)

def get_country_code(database, country):
    """
    1. Receive a dictionary (database) and a key (country).
    2. Return the value associated with that key.
    Example input: {'ZA': 'South Africa', 'US': 'USA'}, 'ZA'
    Example output: 'South Africa'
    """
    # TODO: Write your code here
    return database[country]

database = {"ZA": "South Africa", "JP": "Japan", "BR": "Brazil"}
get_country_code(database, "BR")

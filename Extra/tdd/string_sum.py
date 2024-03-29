# String Calculator

# Before you start:
# Try not to read ahead.
#
# Do one task at a time. The trick is to learn to work incrementally.
#
# Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata
#


# String Calculator
#
# Create a simple String calculator with a method signature:
# ———————————————
# int Add(string numbers)
# ———————————————
# The method can take up to two numbers, separated by commas, and will return their sum.
# for example “” or “1” or “1,2” as inputs.
# (for an empty string it will return 0)
# Hints:
# ——————
#  - Start with the simplest test case of an empty string and move to one and two numbers
#  - Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
#  - Remember to refactor after each passing test

def add(numbers):
    num_list = parse_numbers(numbers)
    sum = 0
    for number in num_list:
        sum = sum + number
    return sum

def parse_numbers(number_string):
    normalized_number_string = number_string.replace("\n", ",")
    list = normalized_number_string.split(",")
    int_list = []
    for number in list:
        if number:
            int_list.append(int(number))
    return int_list





















# ———————————————————————————————
# Allow the Add method to handle an unknown amount of numbers



















# ————————————————————————————————
# Allow the Add method to handle new lines between numbers (instead of commas).
# the following input is ok: “1\n2,3” (will equal 6)
# the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)



















# ——————————————————————————————-
# Support different delimiters
# to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
# the first line is optional. all existing scenarios should still be supported



















# ————————————————————————————————
# Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed.
# if there are multiple negatives, show all of them in the exception message.




















# ————————————————————————————————
# Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2






















# ————————————————————————————————
# Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6




















# ————————————————————————————————
# Allow multiple delimiters like this: “//[delim1][delim2]\n” for example “//[*][%]\n1*2%3” should return 6.



















# ————————————————————————————————
# make sure you can also handle multiple delimiters with length longer than one char
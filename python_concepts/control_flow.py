"""
This an overview of the main control flow Types in Python
These are Lists, Tuples, Dictionaries and Sets
"""
from pprint import pprint


# if else, the most basic statement. this also a function with id defined with def and can take 1 or more arguments
# they are used in oop a lot, help with reusability of of the code! They use the return keyword too
def simple_if_else(is_true):
    if is_true == 'True':
        return 'Yes'
    else:
        return 'No'


# slight variation on if-else, but with the addition of elif
def simple_elif(is_true):
    if is_true == 'True':
        return 'Yes'
    elif is_true == 'Yes':
        return 'Maybe'
    else:
        return 'No'


# simple for loop python, can executed in a range or over a data structure like a list, tuple or string
def example_for_loop():
    for i in range(1, 100):
        print(i)


# while loop in Python, will only execute if that condition is true
# do while is not used in python, but you can use an alternative which executes the code at least once
# as seen below
def example_while_loop():
    number = 10
    while number > 0:
        print(number)
        number -= 1
    # do-while substitute, this way your code will always be executed

    while True:
        user_input = input("Please enter your name?")
        if user_input == 'q':
            print('You quit the program')
            break
        print("You Entered: ", user_input)


# Try catch, tries to catch an error and then executes the code af the except is found
# its best that you try and put the except you know but you can use a generic one too but that's not recommended.
# The finally keyword is used regardless of weather an exception is made or not
# just to mention, you ca generic exception called BaseException but this is not recommended,
# pick the errors you are exception
def example_try_catch():
    # Standard excepts
    try:
        user_input = int(input("Enter a number: "))
        zero = int(input("Don't put in zero!"))
        x = user_input / zero
        print(x)
    except ValueError:
        print("Empty Value!")
    except ZeroDivisionError:
        print("cannot divide by Zero")
    finally:
        print("You are amazing")


# example of break and continue, break terminates
# the loop and sets the i to where it broke,
# if I used continue it would have terminated at the end of the range.
# Continue isn't strictly necessary but good practise
def example_break_continue():
    for i in range(1, 10):
        if i == 5:
            break
    print(i)

    for i in range(0, 11):
        if i == 5:
            continue
    return i


# Pass is used when you want to create an empty function maybe to return to it later
def example_pass():
    pass


# return example to end a function or class. You can also return multiple values as seen below
# its bad practise to return multiple values, much better to retun a list or tuple
def return_example():
    # return a + b
    return 1, 2, 'hello'


# Raise example in Python, allow to use when a
# specific condition occurs, so below i'm raising a Value error when b is equal to 0
def raise_example(a, b):
    if b == 0:
        raise ValueError("Cannot divide by Zero sorry!")
    return a / b


# Assert Keyword in Python, can be use for debugging but otherwise, no recommended
def assert_example(a):
    assert a == 1
    return a


# With keyword used wraps a context manager block. With allows a block of code to acquire and release resources
# for example opening and closing files, __enter__() and then __exit__() functions are called exceptions can  be
# triggered. Certain things will need to done in specific orders like DB connections
# example below, reading and writing a file with a try catch
def with_example():
    with open('example.txt', 'w') as f:
        f.write("Hey how ware you?\n")
        f.write("Today is sunny!")
    try:
        with open('example.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Error")


# Lambda functions, anonymous functions can be used to streamline code
# why they're useful small throwaway functions and used in conjunction with map(), filter() and reduce()
def example_lambda():
    add = lambda a, n: a + n
    main = add(1, 2)
    return main


# List comprehensions
# layout: new_list = [expression for item in iterable]
# easily generates a range without having to using the 'for' loop, saves the item as a variable
# starts with a [] instead of ()
def example_list_comprehensions():
    squares = [x * 0 for x in range(10)]
    return squares


# Generator expressions in Python
# Similar to a List Comprehension but this is used to create an iterator
# Generators a great for large data sets
# starts with a () instead of []
def example_generator_expressions():
    squares = (x ** 2 for x in range(10))
    print(type(squares))
    for square in squares:
        print(square)

    return squares


# Shortened way of writing code in Python
def example_teranery_operator(status):
    status = "online" if not status else "offline"
    return "The status is " + status


# Function calls itself solve a problem, can provide elegant solutions to a problem
# can be useful  when traversing tree like data structures, trees and graphs
# downsides is consumes a lot of memory and can cause a stack overflow
def example_recursion(n):
    if n == 1:
        return 1
    else:
        return n * example_recursion(n - 1)


def example_coroutines():
    pass


if __name__ == "__main__":
    print(example_recursion(5))

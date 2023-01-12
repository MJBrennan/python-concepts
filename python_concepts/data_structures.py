"""
This an overview of the main data structures in Python
These are Lists, Tuples, Dictionaries and Sets
"""


def list_example():
    """
    Lists can be changed and have some functions like append(),
    remove(), sort(), and reverse(). Similar to arrays php.
    Uses squared brackets like php
    """
    example_list = [1, 2, 3, 7]
    example_list.reverse()
    return example_list


def tuple_example():
    """
    Uses curly brackets. Is immutable (can't be changed). Example use case, you have a
    calculator with a set number of operations, store those operation in a Tuple(+,-,x etc)
    """
    example_tuple = (1, 2, 3, 7, "Smith", (0, 1))
    return example_tuple[5]


def dictionary_example():
    """
    key value pair, similar to associative array in php. Uses curly braces, keys can't be repeated
    """

    students = {"Alice": 20, "Bob": 22, "Charlie": [], "Michael": 20}

    # Adding item to dictionary

    # Removing an element form a list

    del students["Charlie"]

    # modifying an item

    students["Bob"] = 20

    # you can use .items() to easily access the dictionary via iteration

    for key, value in students.items():
        str(print(key)) + "/n"

    return students


def set_example():
    """
    Set is a collection of unique items, defined with curly braces, items can be added and removed.
    Use Case: just want to check if its in a collection or not, one nice thing is you can use set operations
    """
    numbers = {1, 2, 3, 4, "Michael"}

    """
    add element to a set
    """
    numbers.add(7)

    """
    remove an element
    """
    numbers.remove(1)

    """
    checking if an element exists in a set
    """
    does_exist = "Tom" in numbers

    print(does_exist)

    names = {"Alice", "Bob", "Charlie", "David"}
    """
    Using Set Operations in Python Sets, can be useful when comparing Sets
    """
    a = {"Tom", "Dick", "Harry"}
    b = {3, 4, 5}

    # Union
    print(a.union(b))  # Output: {1, 2, 3, 4, 5}

    # Intersection
    print(a.intersection(b))  # Output: {3}

    # Difference
    print(a.difference(b))  # Output: {1, 2}

    return numbers


'''
Arrays can be used too, better to use Lists overall by they do have some advantages
1. More memory efficient when using large amounts of data
2. Arrays are faster than Lists

but some disadvantages:
1. Data types are restricted to one, for example would have to be all strings
2. No built in methods for example no add(), remove() etc

'''


def array_example():
    from array import array
    # Creating an array of integers
    numbers = array("i", [1, 2, 3, 4, 5])

    # Creating an array of floating-point numbers
    floats = array("f", [1.1, 2.2, 3.3, 4.4, 5.5])

    return numbers[6]


if __name__ == "__main__":
    print(array_example())

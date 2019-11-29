"""Produce a solution to Python to as many of these challenegs as you can

One challenge is already implemented so you can get get the idea (not
that it's difficult...). You can look up as much as you like on the internet
but I will expect you to understand the code you implement, so don't just
Cargo Cult it

NB Your solution has to return the result, not just print it!
"""

def fizz(until_n):
    """Return the list of numbers starting from 1 up to `until_n`
    replacing multiples of 7 by the word "Fizz"

    eg fizz(20) should return:
    [1, 2, 3, 4, 6, "Fizz", 8, 9 10, 11, 12, 13, "Fizz", 15, 16, 17, 18, 19, 20]
    """
    result = []
    n = 1
    while n <= until_n:
        if n % 7 == 0:
            result.append("Fizz")
        else:
            result.append(n)
        n += 1

    return result


def triangular_numbers(n):
    """Return the list of the first n triangular_numbers

    A triangular number is one which consists of the first n numbers
    added together. So 3 is a triangular number (1 + 2); 6 is a triangular
    number (1 + 2 + 3) and so on.

    eg triangular_numbers(5) should return:
    [1, 3, 6, 10, 15]
    """
    raise NotImplementedError


def backwards(word):
    """Return the word with the letters in the opposite direction

    eg backwards("Timothy") should return:
    "yhtomiT"
    """
    raise NotImplementedError


def secret_santa(people):
    """From a list of people produce a Secret Santa list so everyone gets
    a present but no-one gets themself.

    NB There will be more than one correct answer for any list of people, Ideally,
    calling the function twice for the same group of people won't give the same
    result

    eg secret_santa(['Tim', 'David', 'Peter', 'Tommy', 'Kwame']) might return:
    [('Tim', 'David'), ('David', 'Peter'), ('Peter', 'Tommy'), ('Tommy', 'Kwame'), ('Kwame', 'Tim')]
    """
    raise NotImplementedError


def anagrams(word):
    """Using the words in words.txt find all the anagrams of `word`

    eg anagrams("LATER") would produce:
    ['ALERT', 'ALTER']
    """
    raise NotImplementedError


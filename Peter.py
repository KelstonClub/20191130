"""Produce a solution to Python to as many of these challenegs as you can

One challenge is already implemented so you can get get the idea (not
that it's difficult...). You can look up as much as you like on the internet
but I will expect you to understand the code you implement, so don't just
Cargo Cult it.

There are two aspects to the result:

1) That it passes the test (the "Engineer's" result)
2) That it does is elegantly, efficiently and perhaps interestingly (the "Programmer's" result)

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


def numbers(n):
    """Return a list of the first n numbers

    eg numbers(8) should return:
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    n_list = []
    for i in range(n):
        n_list.append(i)
    n_list.append(i+1)
    return n_list


def odd_numbers(n):
    """Return a list of the first n odd numbers

    eg odd_numbers(5) should return:
    [1, 3, 5, 7, 9]
    """
    n_list = []
    counter = 1
    n_list.append(counter)
    while len(n_list) != n:
        counter = counter+2
        n_list.append(counter)
    return n_list


def factorial(n):
    """Return the factorial of n

    A factorial is a number multiplied by all the numbers before it until 1
    It's written as the number followed by an exclamation mark: 5!
    So 5! = 5 * 4 * 3 * 2 * 1 = 120

    eg factorial(4) should return:
    24
    """
    answer = 1
    counter = 1
    while counter != n+1:
        answer = counter * answer
        counter = counter+1
    return answer


def triangular_numbers(n):
    """Return the list of the first n triangular_numbers

    A triangular number is one which consists of the first n numbers
    added together. So 3 is a triangular number (1 + 2); 6 is a triangular
    number (1 + 2 + 3) and so on.

    eg triangular_numbers(5) should return:
    [1, 3, 6, 10, 15]
    """
    list_answer = []
    number_answer = 1
    n_list = []
    for i in range(n):
        pass

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


def palindromes(n):
    """Using the words in words.txt find all palindromes of n letters

    A palindrome is a word which is spelt the same backwaards and forwards
    eg LEVEL or RADAR
    """
    raise NotImplementedError

if __name__ == '__main__':
    print(triangular_numbers(5))
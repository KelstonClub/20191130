#!python
import unittest

import tommy as challenges

class TestChallenges(unittest.TestCase):

    def test_fizz(self):
        actual = list(challenges.fizz(10))
        expected = [1, 2, 3, 4, 5, 6, 'Fizz', 8, 9, 10]
        self.assertEqual(actual, expected)

    def test_numbers(self):
        actual = list(challenges.numbers(6))
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_odd_numbers(self):
        actual = list(challenges.odd_numbers(8))
        expected = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(actual, expected)

    def test_factorial(self):
        actual = challenges.factorial(6)
        expected = 720
        self.assertEqual(actual, expected)

    def test_triangular_numbers(self):
        actual = list(challenges.triangular_numbers(5))
        expected = [1, 3, 6, 10, 15]
        self.assertEqual(actual, expected)

    def test_backwards(self):
        actual = challenges.backwards("Pomegranate")
        expected = "Pomegranate"[::-1]
        self.assertEqual(actual, expected)

    def test_secret_santa(self):
        candidates = ["Person %d" % (i + 1) for i in range(6)]
        people = set(candidates)
        actual = list(challenges.secret_santa(candidates))
        givers = set(g for g, r in actual)
        recipients = set(r for g, r in actual)
        self.assertEqual(people, givers, "Someone isn't giving")
        self.assertEqual(people, recipients, "Someone isn't receiving")
        for giver, recipient in actual:
            if giver == recipient:
                raise RuntimeError("%s is giving to themself" % giver)

    def test_anagrams(self):
        import itertools
        candidate = "wander"
        actual = set(challenges.anagrams(candidate))
        expected = set(["warned", "redawn", "andrew", "warden"])
        self.assertEqual(actual, expected)

    def test_palindromes(self):
        length = 6
        actual = set(challenges.palindromes(length))
        words = set(w for w in open("words.txt").read().split() if len(w) == length)
        expected = set(w for w in words if w == w[::-1])
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

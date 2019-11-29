import unittest

import tim as challenges

class TestChallenges(unittest.TestCase):

    def test_fizz(self):
        actual = list(challenges.fizz(10))
        expected = [1, 2, 3, 4, 5, 6, 'Fizz', 8, 9, 10]
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
        self.assertEqual(people, givers)
        self.assertEqual(people, recipients)
        for giver, recipient in actual:
            if giver == recipient:
                raise RuntimeError("%s is giving to themself" % giver)

    def test_anagrams(self):
        import itertools
        candidate = "wander"
        actual = set(challenges.anagrams(candidate))
        expected = set(["warned", "redawn", "andrew", "warden"])
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
    if sys.stdout.isatty(): raw_input("Press enter...")

import unittest

import challenges

class TestChallenges(unittest.TestCase):

    def test_fizz(self):
        actual = challenges.fizz(10)
        expected = [1, 2, 3, 4, 5, 6, 'Fizz', 8, 9, 10]
        self.assertEqual(actual, expected)

    def test_factorial(self):
        actual = challenges.factorial(6)
        expected = 720
        self.assertEqual(actual, expected)

    def test_triangular_numbers(self):
        actual = challenges.triangular_numbers(5)
        expected = [1, 2, 3, 6, 10]
        self.assertEqual(actual, expected)

    def test_backwards(self):
        actual = challenges.backwards("Pomegranate")
        expected = "Pomegranate"[::-1]
        self.assertEqual(actual, expected)

    def test_secret_santa(self):
        candidates = ["Person %d" % (i + 1) for i in range(6)]
        people = set(candidates)
        actual = challenges.secret_santa(people)
        givers = set(g for g, r in actual)
        recipients = set(r for g, r in actual)
        self.assertEqual(people, givers)
        self.assertEqual(people, recipients)
        for giver, recipient in actual:
            if giver == recipient:
                raise RuntimeError("%s is giving to themself" % giver)

    def test_anagrams(self):
        import itertools
        candidate = "LETTER"
        actual = challenges.anagrams(candidate)
        words = set(open("words.txt").read().split())
        candidates = set("".join(p) for p in itertools.permutations(candidate))
        candidates.remove(candidate)
        expected = candidates & words
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
    if sys.stdout.isatty(): raw_input("Press enter...")

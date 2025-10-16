from django.test import TestCase

from .models import Function, GuessResult

IDENTITY = Function("identity", ["x"], [[0], [42]], "x")

class FunctionTest(TestCase):
    def test_evaluate(self):
        res = IDENTITY.evaluate([123])
        self.assertEqual(res, 123)

    def test_guess_single_correct(self):
        (res, err) = IDENTITY.guess_single("0", [0]) # not actually correct but with this input you can't tell!
        self.assertEqual(res, GuessResult.CORRECT)
        self.assertEqual(err, None)

    def test_guess_single_incorrect(self):
        (res, err) = IDENTITY.guess_single("0", [1])
        self.assertEqual(res, GuessResult.INCORRECT)
        self.assertEqual(err, None)

    def test_guess_single_error_undefined(self):
        (res, err) = IDENTITY.guess_single("y", [0]) # `y` is not defined
        self.assertEqual(res, GuessResult.ERROR)
        self.assertNotEqual(err, None)

    def test_guess_single_error_argcount(self):
        (res, err) = IDENTITY.guess_single("0", [0, 1]) # 2 args, expected 1
        self.assertEqual(res, GuessResult.ERROR)
        self.assertNotEqual(err, None)

    def test_guess_single_error_timeout(self):
        (res, err) = IDENTITY.guess_single("10 ** 5 ** 10", [0]) # takes quite a long time to evaluate!
        self.assertEqual(res, GuessResult.ERROR)
        self.assertNotEqual(err, None)

    def test_samples_correct(self):
        (res, sample, err) = IDENTITY.guess_samples("x")
        self.assertEqual(res, GuessResult.CORRECT)
        self.assertEqual(sample, None)
        self.assertEqual(err, None)

    def test_samples_incorrect(self):
        (res, sample, err) = IDENTITY.guess_samples("0") # only correct for 1st sample
        self.assertEqual(res, GuessResult.INCORRECT)
        self.assertEqual(sample, [42])
        self.assertEqual(err, None)

    def test_samples_error(self):
        (res, sample, err) = IDENTITY.guess_samples("y") # `y` is not defined
        self.assertEqual(res, GuessResult.ERROR)
        self.assertEqual(sample, [0])
        self.assertNotEqual(err, None)

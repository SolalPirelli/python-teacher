from dataclasses import dataclass
from enum import Enum
from multiprocessing import Pool, TimeoutError
from typing import *

TIMEOUT = 2 # seconds

class GuessResult(Enum):
    """Result of evaluating a user's guess for a function."""
    CORRECT = 0
    INCORRECT = 1
    ERROR = 2

@dataclass
class Function:
    """Integer function whose code the user has to figure out by themselves."""
    description: str
    parameters: List[str]
    sample_inputs: List[List[int]]
    hints: List[str]
    code: str

    def evaluate(self, args: List[int]) -> int:
        """Evaluates this function with the given arguments. Assumes there are exactly as many arguments as the function has parameters."""
        locals = dict(zip(self.parameters, args))
        return eval(self.code, {}, locals)

    def guess_single(self, attempt: str, args: List[int]) -> (GuessResult, Optional[str]):
        """
        Compares the given attempt, as Python code, to this function for the given arguments.
        Does not assume anything about the attempt or arguments.
        Returns a guess result and, if it is an error, an error message.
        """
        if len(args) != len(self.parameters):
            return (GuessResult.ERROR, "Wrong number of arguments.")

        # based on https://stackoverflow.com/a/51619876/3311770
        with Pool(processes=2) as pool:
            locals = dict(zip(self.parameters, args))
            result = pool.apply_async(eval, [attempt, None, locals])

            try:
                r = result.get(timeout=TIMEOUT)
                if r == self.evaluate(args):
                    return (GuessResult.CORRECT, None)
                return (GuessResult.INCORRECT, None)
            except TimeoutError:
                return (GuessResult.ERROR, "Timeout. The code took too long to evaluate.")
            except Exception as e:
                return (GuessResult.ERROR, str(e))

    def guess_samples(self, attempt: str) -> (GuessResult, Optional[List[int]], Optional[str]):
        """
        Compares the given attempt, as Python code, to this function for its sample inputs.
        Does not assume anything about the attempt.
        Returns a guess result and, if the result is not CORRECT, a sample input that failed, and if the result is ERROR, an error message.
        """
        for sample in self.sample_inputs:
            (res, err) = self.guess_single(attempt, sample)
            if res == GuessResult.INCORRECT:
                return (res, sample, None)
            if res == GuessResult.ERROR:
                return (res, sample, err)
        return (GuessResult.CORRECT, None, None)

@dataclass
class FunctionExample:
    """Example inputs/output pair for an integer function."""
    inputs: List[int]
    output: int

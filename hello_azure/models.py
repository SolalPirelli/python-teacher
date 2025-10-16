from dataclasses import dataclass
from enum import Enum
from typing import *

class GuessResult(Enum):
    CORRECT = 0
    INCORRECT = 1
    ERROR = 2

@dataclass
class Function:
    """Integer function whose code the user has to figure out by themselves."""
    description: str
    parameters: List[str]
    sample_inputs: List[List[int]]
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
        return (GuessResult.CORRECT, None)

    def guess_samples(self, attempt: str) -> (GuessResult, Optional[List[int]], Optional[str]):
        """
        Compares the given attempt, as Python code, to this function for its sample inputs.
        Does not assume anything about the attempt.
        Returns a guess result and, if the result is not CORRECT, a sample input that failed, and if the result is ERROR, an error message.
        """
        return (GuessResult.CORRECT, None, None)

@dataclass
class FunctionExample:
    """Example inputs/output pair for an integer function."""
    inputs: List[int]
    output: int

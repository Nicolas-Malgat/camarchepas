import pytest
from PCF import *

class TestClass():
    
    @pytest.mark.parametrize(
        "A, B",
        [
            (Choice.ROCK, Choice.PAPER),
            (Choice.SCISSORS, Choice.PAPER),
            (Choice.SCISSORS, Choice.SCISSORS)
        ]
    )
    def test_is_win_expect_WIN(A, B):
        assert

    @pytest.mark.parametrize(
        "A, B",
        [
            (Choice.ROCK, Choice.PAPER),
            (Choice.SCISSORS, Choice.PAPER),
            (Choice.SCISSORS, Choice.SCISSORS)
        ]
    )
    def test_is_win_expect_LOOSE(A, B):
        assert

    @pytest.mark.parametrize(
        "A, B",
        [
            (Choice.ROCK, Choice.PAPER),
            (Choice.SCISSORS, Choice.PAPER),
            (Choice.SCISSORS, Choice.SCISSORS)
        ]
    )
    def test_is_win_expect_TIE(A, B):
        assert
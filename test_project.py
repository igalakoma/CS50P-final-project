from project import rps_convert
from project import rps_score
from project import game_2
from project import game_3
from unittest.mock import patch

# testing game_2 (HANGMAN)
def test_game_2_wins():
    @patch('random.choice', lambda _: "PYTHON")
    @patch('builtins.input', side_effect=["P", "A", "Y", "B", "T", "H", "O", "N"])
    def run_test(mock_input):
        score = game_2()
        assert score == 300

def test_game_2_loses():
    @patch('random.choice', lambda _: "PYTHON")
    @patch('builtins.input', side_effect=["A", "B", "C", "D", "E", "F", "G", "I", "J", "K"])
    def run_test(mock_input):
        score = game_2()
        assert score == 0



# testing game_3 (ROCK, PAPER, SCISSORS)

# testing converting function
def test_rps_convert():
    # Rock
    assert rps_convert("rock") == """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

    # Paper
    assert rps_convert("paper") == """
        _______
    ---'    ____)_
            ______)
            _______)
            _______)
    ---.__________)
    """

    # Scissors
    assert rps_convert("scissors") =="""
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    """

# testing score function
def test_rps_score_wins():
    assert(rps_score("rock","scissors")) == (1,0)
    assert(rps_score("paper","rock")) == (1,0)
    assert(rps_score("scissors","paper")) == (1,0)

def test_rps_score_loses():
    assert(rps_score("rock","paper")) == (0,1)
    assert(rps_score("scissors","rock")) == (0,1)
    assert(rps_score("paper","scissors")) == (0,1)

# testing game_3
def test_rps_wins():
    @patch('builtins.input', side_effect=["rock", "paper", "rock"])
    @patch('random.choice', lambda _: "scissors")
    def run_test(mock_input):
        score = game_3()
        assert score == 300

def test_rps_loses():
    @patch('builtins.input', side_effect=["rock", "scissors", "rock"])
    @patch('random.choice', lambda _: "paper")
    def run_test(mock_input):
        score = game_3()
        assert score == 0



if __name__ == "__main__":
    test_game_2_wins()
    test_game_2_loses()
    test_rps_convert()
    test_rps_score_wins()
    test_rps_score_loses()
    test_rps_wins()
    test_rps_loses()


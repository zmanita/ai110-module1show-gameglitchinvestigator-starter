from logic_utils import check_guess

def test_winning_guess():
    # FIXME: check_guess returns a tuple (outcome, message), not just the outcome string
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # FIXME: check_guess returns a tuple (outcome, message), not just the outcome string
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # FIXME: check_guess returns a tuple (outcome, message), not just the outcome string
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_messages():
    """Test that hint messages correctly guide the player."""
    # Test win message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message or "correct" in message.lower()
    
    # Test too high hint message (should tell player to go LOWER)
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER" in message or "LOWER" in message
    
    # Test too low hint message (should tell player to go HIGHER)
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER" in message or "HIGHER" in message

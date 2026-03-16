from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


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

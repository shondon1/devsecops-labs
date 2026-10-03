from app import greet

def test_greet():
    """
    Test the greet function to ensure it returns the expected greeting message.
    """
    name = "Shondon"
    expected_greeting = "Hello, Alice!"
    assert greet(name) == "Shondon"
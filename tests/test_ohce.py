from ohce import Ohce

def test_reverse_echo():
    """Test that the reverse_echo function returns the reversed text."""
    # Arrange
    ohce = Ohce("Pedro")
    
    # Act
    result = ohce.reverse_echo("hola")
    
    # Assert
    assert result == "aloh"

def test_palindrome_detection():
    """Test that detects palindromes and adds '¡Bonita palabra!'."""
    # Arrange
    ohce = Ohce("Pedro")
    
    # Act
    result = ohce.reverse_echo("oto")
    
    # Assert
    assert result == "oto\n¡Bonita palabra!"

class MockClock:
    def __init__(self, hour):
        self.hour = hour
    
    def get_current_hour(self):
        return self.hour

def test_greeting_morning():
    """Test that correctly greets in the morning (between 6 and 12)."""
    # Arrange
    clock = MockClock(8)  # 8:00 AM
    ohce = Ohce("Pedro", clock)
    
    # Act
    greeting = ohce.greet()
    
    # Assert
    assert greeting == "¡Buenos días Pedro!"

def test_greeting_afternoon():
    """Test that correctly greets in the afternoon (between 12 and 20)."""
    # Arrange
    clock = MockClock(15)  # 3:00 PM
    ohce = Ohce("Pedro", clock)
    
    # Act
    greeting = ohce.greet()
    
    # Assert
    assert greeting == "¡Buenas tardes Pedro!"

def test_greeting_night():
    """Test that correctly greets at night (between 20 and 6)."""
    # Arrange
    clock = MockClock(22)  # 10:00 PM
    ohce = Ohce("Pedro", clock)
    
    # Act
    greeting = ohce.greet()
    
    # Assert
    assert greeting == "¡Buenas noches Pedro!"
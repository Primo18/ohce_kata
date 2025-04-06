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
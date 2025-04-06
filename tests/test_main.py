import io
import sys
from unittest.mock import patch
from main import main
from ohce import Ohce

class MockClock:
    def __init__(self, hour):
        self.hour = hour
    
    def get_current_hour(self):
        return self.hour

@patch('sys.stdout', new_callable=io.StringIO)
@patch('builtins.input', side_effect=['hola', 'oto', 'Stop!'])
def test_main_flow(mock_input, mock_stdout):
    """Test of the main program flow."""
    # Arrange
    clock = MockClock(8)  # 8:00 AM
    
    # Act
    main(name="Pedro", clock=clock)
    
    # Assert
    output = mock_stdout.getvalue()
    assert "¡Buenos días Pedro!" in output
    assert "aloh" in output
    assert "oto" in output
    assert "¡Bonita palabra!" in output
    assert "Adios Pedro" in output
from datetime import datetime

class RealClock:
    """Provides the current hour from the system clock."""
    def get_current_hour(self):
        return datetime.now().hour

class Ohce:
    """
    Ohce is a console application that echoes the reverse of what you input through the console.
    It has special behaviors for palindromes and greetings based on time of day.
    """
    
    # Time ranges for different greetings
    MORNING_START = 6
    MORNING_END = 12
    AFTERNOON_END = 20
    
    def __init__(self, name, clock=None):
        """
        Initialize Ohce with a user name and optional clock.
        
        Args:
            name (str): The user's name for personalized messages
            clock: An object with get_current_hour method (dependency injection for testing)
        """
        self.name = name
        self.clock = clock or RealClock()
        self._running = True
        
    def reverse_echo(self, text):
        """
        Reverses the input text and adds a special message for palindromes.
        
        Args:
            text (str): The text to reverse
            
        Returns:
            str: The reversed text with special message if it's a palindrome
        """
        reversed_text = text[::-1]
        
        if self._is_palindrome(text):
            return f"{reversed_text}\n¡Bonita palabra!"
        
        return reversed_text
    
    def _is_palindrome(self, text):
        """
        Check if a text is a palindrome.
        
        Args:
            text (str): The text to check
            
        Returns:
            bool: True if the text is a palindrome, False otherwise
        """
        return text == text[::-1]
    
    def greet(self):
        """
        Creates a greeting based on the current time of day.
        
        Returns:
            str: A time-appropriate greeting including the user's name
        """
        hour = self.clock.get_current_hour()
        
        if self.MORNING_START <= hour < self.MORNING_END:
            return f"¡Buenos días {self.name}!"
        elif self.MORNING_END <= hour < self.AFTERNOON_END:
            return f"¡Buenas tardes {self.name}!"
        else:  # 20-23 and 0-5
            return f"¡Buenas noches {self.name}!"
    
    def process_input(self, text):
        """
        Process user input, handling special commands and normal text.
        
        Args:
            text (str): The user input text
            
        Returns:
            str: The response to the user input
        """
        if text == "Stop!":
            self._running = False
            return f"Adios {self.name}"
        
        return self.reverse_echo(text)
    
    def is_running(self):
        """
        Check if the application is still running.
        
        Returns:
            bool: True if the application is running, False if it should stop
        """
        return self._running